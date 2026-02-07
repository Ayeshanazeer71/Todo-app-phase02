"""
TodoManager class for the Todo Console Application
Handles all business logic for task operations
"""
from typing import List, Optional
from .models import Task


class TodoManager:
    """
    Core business logic for task operations
    """
    def __init__(self) -> None:
        self.tasks: List[Task] = []
        self._next_id: int = 1

    def get_next_id(self) -> int:
        """Get the next available ID and increment the counter"""
        current_id = self._next_id
        self._next_id += 1
        return current_id

    def add_task(self, title: str, description: str = "") -> int:
        """
        Add a new task with the given title and description
        Returns the ID of the newly created task
        """
        task_id = self.get_next_id()
        task = Task(id=task_id, title=title, description=description, completed=False)
        self.tasks.append(task)
        return task_id

    def list_tasks(self) -> List[Task]:
        """
        Return a list of all tasks
        """
        return self.tasks.copy()

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a task by its ID, returns None if not found
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Update a task's title and/or description by ID
        Returns True if successful, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        if title is not None:
            task.title = title
        if description is not None:
            task.description = description

        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by ID
        Returns True if successful, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        self.tasks.remove(task)
        return True

    def toggle_task_status(self, task_id: int) -> bool:
        """
        Toggle the completion status of a task by ID
        Returns True if successful, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        task.completed = not task.completed
        return True