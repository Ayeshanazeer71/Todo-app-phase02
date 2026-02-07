"use client";

import { useEffect, useState } from "react";
import { api } from "@/lib/api";
import { useRouter } from "next/navigation";
import {
  DndContext,
  closestCenter,
  KeyboardSensor,
  PointerSensor,
  useSensor,
  useSensors,
  DragEndEvent,
} from "@dnd-kit/core";
import {
  arrayMove,
  SortableContext,
  sortableKeyboardCoordinates,
  verticalListSortingStrategy,
  useSortable,
} from "@dnd-kit/sortable";
import { CSS } from "@dnd-kit/utilities";
import {
  ListTodo,
  LogOut,
  Plus,
  Search,
  GripVertical,
  Calendar,
  Tag,
  ChevronDown,
  CheckCircle2,
  Circle,
  Trash2,
  Pencil,
  ClipboardList,
  Loader2,
} from "lucide-react";

type FilterStatus = "all" | "active" | "completed";
type Priority = "low" | "medium" | "high";

interface Subtask {
  title: string;
  completed: boolean;
}

interface Task {
  id: number;
  title: string;
  description?: string;
  completed: boolean;
  deadline?: string;
  priority: Priority;
  category: string;
  subtasks: Subtask[];
  position: number;
}

function SortableTaskItem({
  task,
  onToggle,
  onDelete,
  onEdit,
  priorityColors
}: {
  task: Task;
  onToggle: (id: number) => void;
  onDelete: (id: number) => void;
  onEdit: (task: Task) => void;
  priorityColors: any;
}) {
  const {
    attributes,
    listeners,
    setNodeRef,
    transform,
    transition,
    isDragging,
  } = useSortable({ id: task.id });

  const style = {
    transform: CSS.Transform.toString(transform),
    transition,
    zIndex: isDragging ? 10 : 1,
    opacity: isDragging ? 0.5 : 1,
  };

  const subtasks = task.subtasks || [];
  const completedSubtasks = subtasks.filter(s => s.completed).length;
  const progress = subtasks.length > 0 ? (completedSubtasks / subtasks.length) * 100 : 0;
  const isOverdue = task.deadline && new Date(task.deadline) < new Date() && !task.completed;

  return (
    <div
      ref={setNodeRef}
      style={style}
      className={`group relative flex items-start gap-4 p-5 bg-white rounded-2xl shadow-sm border transition-all duration-200 min-h-[88px] ${isDragging ? "shadow-lg border-blue-200 scale-[1.02] ring-2 ring-blue-100" : "border-gray-100 hover:border-gray-200 hover:shadow-md"} ${task.completed ? "opacity-90" : ""}`}
    >
      <div {...attributes} {...listeners} className="cursor-grab active:cursor-grabbing pt-0.5 text-gray-300 hover:text-gray-500 touch-none">
        <GripVertical className="h-5 w-5" />
      </div>
      <button type="button" onClick={() => onToggle(task.id)} className="shrink-0 mt-0.5 text-gray-300 hover:text-blue-500 transition-colors" aria-label={task.completed ? "Mark incomplete" : "Mark complete"}>
        {task.completed ? <CheckCircle2 className="h-6 w-6 text-green-500" /> : <Circle className="h-6 w-6" strokeWidth={2} />}
      </button>
      <div className="flex-1 min-w-0">
        <div className="flex flex-wrap items-center gap-2 mb-1">
          <h3 className={`text-base font-semibold truncate ${task.completed ? "line-through text-gray-400" : "text-gray-800"}`}>{task.title}</h3>
          <span className={`text-[10px] px-2 py-0.5 rounded-full font-medium uppercase tracking-wide ${priorityColors[task.priority]}`}>{task.priority}</span>
          <span className="text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium flex items-center gap-1">
            <Tag className="h-3 w-3" />
            {task.category}
          </span>
        </div>
        {task.description && (
          <p className={`text-sm leading-relaxed mb-2 line-clamp-2 ${task.completed ? "text-gray-300" : "text-gray-500"}`}>{task.description}</p>
        )}
        {subtasks.length > 0 && (
          <div className="mb-2">
            <div className="flex justify-between text-[10px] font-medium text-gray-400 mb-1">
              <span>Progress</span>
              <span>{completedSubtasks}/{subtasks.length}</span>
            </div>
            <div className="h-1.5 w-full bg-gray-100 rounded-full overflow-hidden">
              <div className="h-full bg-blue-500 rounded-full transition-all duration-500" style={{ width: `${progress}%` }} />
            </div>
          </div>
        )}
        {task.deadline && (
          <div className={`flex items-center gap-1.5 text-xs font-medium ${isOverdue ? "text-red-500" : "text-gray-400"}`}>
            <Calendar className="h-3.5 w-3.5 shrink-0" />
            <span>{new Date(task.deadline).toLocaleDateString(undefined, { month: "short", day: "numeric", year: "numeric" })}</span>
          </div>
        )}
      </div>
      <div className="flex items-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity shrink-0">
        <button type="button" onClick={() => onEdit(task)} className="p-2 text-gray-400 hover:text-blue-600 hover:bg-blue-50 rounded-lg transition-colors" aria-label="Edit task">
          <Pencil className="h-4 w-4" />
        </button>
        <button type="button" onClick={() => onDelete(task.id)} className="p-2 text-gray-400 hover:text-red-600 hover:bg-red-50 rounded-lg transition-colors" aria-label="Delete task">
          <Trash2 className="h-4 w-4" />
        </button>
      </div>
    </div>
  );
}

export default function TasksPage() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState(true);
  const [mounted, setMounted] = useState(false);
  const [newTitle, setNewTitle] = useState("");
  const [newDescription, setNewDescription] = useState("");
  const [newDeadline, setNewDeadline] = useState("");
  const [newPriority, setNewPriority] = useState<Priority>("medium");
  const [newCategory, setNewCategory] = useState("General");
  const [filter, setFilter] = useState<FilterStatus>("all");
  const [categoryFilter, setCategoryFilter] = useState("all");
  const [searchQuery, setSearchQuery] = useState("");
  const [editingTask, setEditingTask] = useState<Task | null>(null);

  const router = useRouter();

  const sensors = useSensors(
    useSensor(PointerSensor),
    useSensor(KeyboardSensor, {
      coordinateGetter: sortableKeyboardCoordinates,
    })
  );

  useEffect(() => {
    setMounted(true);
    const token = localStorage.getItem("auth_token");
    if (!token) {
      router.push("/login");
      return;
    }
    loadTasks();
  }, [router]);

  if (!mounted) return null;

  async function loadTasks() {
    try {
      const data = await api.getTasks();
      setTasks(data);
    } catch (err: any) {
      if (err.message.includes("401") || err.message.includes("credentials")) {
        api.logout();
      }
      console.error(err);
    } finally {
      setLoading(false);
    }
  }

  async function handleCreateTask(e: React.FormEvent) {
    e.preventDefault();
    if (!newTitle) return;
    try {
      const newTask = await api.createTask({
        title: newTitle,
        description: newDescription || undefined,
        deadline: newDeadline || undefined,
        priority: newPriority,
        category: newCategory || "General",
        subtasks: [],
        position: tasks.length
      } as any);
      setTasks([...tasks, newTask]);
      setNewTitle("");
      setNewDescription("");
      setNewDeadline("");
      setNewPriority("medium");
      setNewCategory("General");
    } catch (err) {
      alert(err);
    }
  }

  async function handleUpdateTask(e: React.FormEvent) {
    e.preventDefault();
    if (!editingTask) return;
    try {
      const updated = await api.updateTask(editingTask.id, {
        title: editingTask.title,
        description: editingTask.description,
        deadline: editingTask.deadline || null,
        priority: editingTask.priority,
        category: editingTask.category || "General",
        subtasks: editingTask.subtasks
      });
      setTasks(tasks.map(t => t.id === editingTask.id ? updated : t));
      setEditingTask(null);
    } catch (err) {
      alert(err);
    }
  }

  async function handleToggle(id: number) {
    try {
      const updated = await api.toggleComplete(id);
      setTasks(tasks.map(t => t.id === id ? updated : t));
    } catch (err) {
      alert(err);
    }
  }

  async function handleDelete(id: number) {
    if (!confirm("Are you sure?")) return;
    try {
      await api.deleteTask(id);
      setTasks(tasks.filter(t => t.id !== id));
    } catch (err) {
      alert(err);
    }
  }

  const handleDragEnd = async (event: DragEndEvent) => {
    const { active, over } = event;
    if (over && active.id !== over.id) {
      const oldIndex = tasks.findIndex((t) => t.id === active.id);
      const newIndex = tasks.findIndex((t) => t.id === over.id);
      const newTasks = arrayMove(tasks, oldIndex, newIndex);

      // Local update
      setTasks(newTasks);

      // Sync with backend (smallest viable change: only update the moved items position)
      try {
        await api.updateTask(active.id as number, { position: newIndex });
      } catch (err) {
        console.error("Failed to sync order:", err);
      }
    }
  };

  const handleAddSubtask = () => {
    if (!editingTask) return;
    const title = prompt("Subtask title:");
    if (title) {
      setEditingTask({
        ...editingTask,
        subtasks: [...(editingTask.subtasks || []), { title, completed: false }]
      });
    }
  };

  const handleToggleSubtask = (subtaskIndex: number) => {
    if (!editingTask) return;
    const newSubtasks = [...editingTask.subtasks];
    newSubtasks[subtaskIndex].completed = !newSubtasks[subtaskIndex].completed;
    setEditingTask({ ...editingTask, subtasks: newSubtasks });
  };

  const categories = ["all", ...Array.from(new Set(tasks.map(t => t.category)))];

  const filteredTasks = tasks.filter((task) => {
    const matchesStatus =
      filter === "all" ||
      (filter === "active" && !task.completed) ||
      (filter === "completed" && task.completed);

    const matchesCategory = categoryFilter === "all" || task.category === categoryFilter;

    const matchesSearch =
      task.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
      (task.description?.toLowerCase().includes(searchQuery.toLowerCase())) ||
      (task.category.toLowerCase().includes(searchQuery.toLowerCase()));

    return matchesStatus && matchesCategory && matchesSearch;
  });

  const priorityColors = {
    low: "bg-blue-50 text-blue-600 border-blue-100",
    medium: "bg-yellow-50 text-yellow-600 border-yellow-100",
    high: "bg-red-50 text-red-600 border-red-100",
  };

  const total = tasks.length;
  const completed = tasks.filter((t) => t.completed).length;
  const active = total - completed;

  return (
    <main className="min-h-screen bg-gradient-to-b from-slate-50 via-white to-blue-50/20">
      <header className="sticky top-0 z-10 border-b border-gray-100 bg-white/80 backdrop-blur-md">
        <div className="max-w-xl mx-auto px-4 py-4 flex justify-between items-center">
          <div className="flex items-center gap-2">
            <div className="p-2 rounded-xl bg-blue-100 text-blue-600">
              <ListTodo className="h-6 w-6" />
            </div>
            <h1 className="text-xl font-bold text-gray-800">My Tasks</h1>
          </div>
          <button
            onClick={() => api.logout()}
            className="flex items-center gap-2 px-3 py-2 text-sm font-medium text-gray-500 hover:text-red-600 hover:bg-red-50 rounded-lg transition-colors"
          >
            <LogOut className="h-4 w-4" />
            Logout
          </button>
        </div>
      </header>

      <div className="max-w-xl mx-auto px-4 py-6 pb-24">
        <div className="grid grid-cols-3 gap-3 mb-6">
          <div className="bg-white rounded-2xl p-4 shadow-sm border border-gray-100 flex flex-col gap-1">
            <div className="flex items-center gap-2 text-gray-400">
              <ListTodo className="h-4 w-4" />
              <span className="text-[10px] font-semibold uppercase tracking-wider">Total</span>
            </div>
            <p className="text-2xl font-bold text-gray-800 tabular-nums">{total}</p>
          </div>
          <div className="bg-white rounded-2xl p-4 shadow-sm border border-gray-100 flex flex-col gap-1">
            <div className="flex items-center gap-2 text-blue-500">
              <Circle className="h-4 w-4" strokeWidth={2.5} />
              <span className="text-[10px] font-semibold uppercase tracking-wider">Active</span>
            </div>
            <p className="text-2xl font-bold text-blue-600 tabular-nums">{active}</p>
          </div>
          <div className="bg-white rounded-2xl p-4 shadow-sm border border-gray-100 flex flex-col gap-1">
            <div className="flex items-center gap-2 text-green-500">
              <CheckCircle2 className="h-4 w-4" />
              <span className="text-[10px] font-semibold uppercase tracking-wider">Done</span>
            </div>
            <p className="text-2xl font-bold text-green-600 tabular-nums">{completed}</p>
          </div>
        </div>

      {!editingTask ? (
        <form onSubmit={handleCreateTask} className="mb-8 p-5 bg-white rounded-2xl border border-gray-100 shadow-sm space-y-4">
          <div className="flex items-center gap-2 text-gray-700 font-semibold">
            <Plus className="h-5 w-5 text-blue-500" />
            <span>Add New Task</span>
          </div>
          <div className="space-y-3">
            <input
              type="text"
              value={newTitle}
              onChange={(e) => setNewTitle(e.target.value)}
              placeholder="What needs to be done?"
              className="w-full px-4 py-3 border border-gray-100 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none font-medium placeholder:text-gray-400 transition-shadow"
              required
            />
            <textarea
              value={newDescription}
              onChange={(e) => setNewDescription(e.target.value)}
              placeholder="Add details (optional)..."
              className="w-full px-4 py-3 border border-gray-100 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none text-sm resize-none h-20 placeholder:text-gray-400 transition-shadow"
            />
            <div className="grid grid-cols-2 gap-3">
              <div className="space-y-1">
                <label className="text-[11px] font-semibold text-gray-500 uppercase tracking-wider flex items-center gap-1">
                  <Calendar className="h-3 w-3" /> Deadline
                </label>
                <input
                  type="date"
                  value={newDeadline}
                  onChange={(e) => setNewDeadline(e.target.value)}
                  className="w-full px-3 py-2.5 border border-gray-100 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none"
                />
              </div>
              <div className="space-y-1">
                <label className="text-[11px] font-semibold text-gray-500 uppercase tracking-wider">Priority</label>
                <select
                  value={newPriority}
                  onChange={(e) => setNewPriority(e.target.value as Priority)}
                  className="w-full px-3 py-2.5 border border-gray-100 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none capitalize"
                >
                  <option value="low">Low</option>
                  <option value="medium">Medium</option>
                  <option value="high">High</option>
                </select>
              </div>
            </div>
            <div className="space-y-1">
              <label className="text-[11px] font-semibold text-gray-500 uppercase tracking-wider flex items-center gap-1">
                <Tag className="h-3 w-3" /> Category
              </label>
              <input
                type="text"
                value={newCategory}
                onChange={(e) => setNewCategory(e.target.value)}
                placeholder="Work, Personal, etc."
                className="w-full px-3 py-2.5 border border-gray-100 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none"
              />
            </div>
          </div>
          <button type="submit" className="w-full bg-blue-600 text-white py-3.5 rounded-xl hover:bg-blue-700 font-semibold transition-all shadow-md shadow-blue-200/50 hover:shadow-lg active:scale-[0.99] flex items-center justify-center gap-2">
            <Plus className="h-5 w-5" />
            Create Task
          </button>
        </form>
      ) : (
        <form onSubmit={handleUpdateTask} className="mb-8 p-5 bg-blue-50/80 rounded-2xl border border-blue-100 shadow-sm space-y-4">
          <div className="flex items-center gap-2">
            <Pencil className="h-4 w-4 text-blue-600" />
            <h2 className="text-sm font-bold text-blue-700">Editing Task</h2>
          </div>
          <div className="space-y-3">
            <input
              type="text"
              value={editingTask.title}
              onChange={(e) => setEditingTask({...editingTask, title: e.target.value})}
              className="w-full px-4 py-3 border-none bg-white rounded-xl focus:ring-2 focus:ring-blue-500 outline-none font-medium"
              required
            />
            <textarea
              value={editingTask.description || ""}
              onChange={(e) => setEditingTask({...editingTask, description: e.target.value})}
              className="w-full px-4 py-3 border-none bg-white rounded-xl focus:ring-2 focus:ring-blue-500 outline-none text-sm resize-none h-20"
            />

            <div className="space-y-2">
              <div className="flex justify-between items-center">
                <label className="text-[11px] uppercase font-bold text-blue-400 ml-1">Subtasks</label>
                <button
                  type="button"
                  onClick={handleAddSubtask}
                  className="text-[10px] bg-blue-100 text-blue-600 px-2 py-0.5 rounded font-bold"
                >
                  + Add
                </button>
              </div>
              <div className="space-y-1 max-h-32 overflow-y-auto">
                {editingTask.subtasks?.map((st, i) => (
                  <div key={i} className="flex items-center gap-2 bg-white/50 p-2 rounded-lg">
                    <input
                      type="checkbox"
                      checked={st.completed}
                      onChange={() => handleToggleSubtask(i)}
                      className="w-4 h-4"
                    />
                    <span className="text-sm">{st.title}</span>
                  </div>
                ))}
              </div>
            </div>

            <div className="grid grid-cols-2 gap-4">
              <div className="space-y-1">
                <label className="text-[11px] uppercase font-bold text-blue-400 ml-1">Deadline</label>
                <input
                  type="date"
                  value={editingTask.deadline || ""}
                  onChange={(e) => setEditingTask({...editingTask, deadline: e.target.value})}
                  className="w-full px-3 py-2 bg-white rounded-lg text-sm border-none focus:ring-2 focus:ring-blue-500 outline-none"
                />
              </div>
              <div className="space-y-1">
                <label className="text-[11px] uppercase font-bold text-blue-400 ml-1">Priority</label>
                <select
                  value={editingTask.priority}
                  onChange={(e) => setEditingTask({...editingTask, priority: e.target.value as Priority})}
                  className="w-full px-3 py-2 bg-white rounded-lg text-sm border-none focus:ring-2 focus:ring-blue-500 outline-none capitalize"
                >
                  <option value="low">Low</option>
                  <option value="medium">Medium</option>
                  <option value="high">High</option>
                </select>
              </div>
            </div>
          </div>
          <div className="flex gap-3">
            <button type="submit" className="flex-1 bg-blue-600 text-white py-3 rounded-xl hover:bg-blue-700 font-bold transition-all shadow-md active:scale-[0.98]">
              Save Updates
            </button>
            <button
              type="button"
              onClick={() => setEditingTask(null)}
              className="px-6 py-3 bg-white text-gray-500 rounded-xl hover:bg-gray-100 font-bold transition-all border border-gray-100"
            >
              Cancel
            </button>
          </div>
        </form>
      )}

      <section className="mb-6">
        <div className="relative mb-4">
          <Search className="absolute left-4 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400 pointer-events-none" />
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="Search tasks..."
            className="w-full pl-11 pr-4 py-3 bg-white border border-gray-100 rounded-xl shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none text-sm placeholder:text-gray-400"
          />
        </div>
        <div className="flex flex-wrap items-center gap-2">
          <div className="flex bg-gray-100 p-1 rounded-xl">
            {(["all", "active", "completed"] as FilterStatus[]).map((s) => (
              <button
                key={s}
                type="button"
                onClick={() => setFilter(s)}
                className={`flex items-center gap-1.5 px-3 py-2 rounded-lg text-xs font-semibold capitalize transition-all ${
                  filter === s ? "bg-white shadow text-blue-600" : "text-gray-500 hover:text-gray-700"
                }`}
              >
                {s === "all" && <ListTodo className="h-3.5 w-3.5" />}
                {s === "active" && <Circle className="h-3.5 w-3.5" strokeWidth={2.5} />}
                {s === "completed" && <CheckCircle2 className="h-3.5 w-3.5" />}
                {s}
              </button>
            ))}
          </div>
          <div className="relative">
            <Tag className="absolute left-3 top-1/2 -translate-y-1/2 h-3.5 w-3.5 text-gray-400 pointer-events-none" />
            <select
              value={categoryFilter}
              onChange={(e) => setCategoryFilter(e.target.value)}
              className="pl-9 pr-8 py-2 bg-gray-100 rounded-xl text-xs font-semibold text-gray-600 border-0 focus:ring-2 focus:ring-blue-500 outline-none capitalize appearance-none"
            >
              <option value="all">All categories</option>
              {categories.filter(c => c !== "all").map(c => (
                <option key={c} value={c}>{c}</option>
              ))}
            </select>
            <ChevronDown className="absolute right-2 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400 pointer-events-none" />
          </div>
        </div>
      </section>

      <div className="space-y-3">
        {loading ? (
          <div className="flex flex-col items-center justify-center py-16 gap-4">
            <Loader2 className="h-10 w-10 text-blue-500 animate-spin" />
            <p className="text-sm font-medium text-gray-500">Loading your tasks...</p>
          </div>
        ) : (
          <DndContext
            sensors={sensors}
            collisionDetection={closestCenter}
            onDragEnd={handleDragEnd}
          >
            <SortableContext
              items={filteredTasks.map(t => t.id)}
              strategy={verticalListSortingStrategy}
            >
              {filteredTasks.map((task) => (
                <SortableTaskItem
                  key={task.id}
                  task={task}
                  onToggle={handleToggle}
                  onDelete={handleDelete}
                  onEdit={setEditingTask}
                  priorityColors={priorityColors}
                />
              ))}
            </SortableContext>
          </DndContext>
        )}
        {!loading && filteredTasks.length === 0 && (
          <div className="text-center py-16 px-6 bg-white rounded-2xl border-2 border-dashed border-gray-200">
            <div className="w-20 h-20 bg-blue-50 rounded-2xl flex items-center justify-center mx-auto mb-4">
              <ClipboardList className="h-10 w-10 text-blue-400" />
            </div>
            <h3 className="text-gray-700 font-semibold mb-1">No tasks here</h3>
            <p className="text-sm text-gray-500 max-w-xs mx-auto">
              {searchQuery
                ? `No tasks match "${searchQuery}". Try a different search or filter.`
                : filter !== "all"
                  ? `No ${filter} tasks yet. Add one above or switch to "All".`
                  : "Add your first task above to get started."}
            </p>
          </div>
        )}
      </div>
      </div>
    </main>
  );
}
