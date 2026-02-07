"""
Unit tests for the add task functionality
"""
import unittest
from src.todo_manager import TodoManager


class TestAddTask(unittest.TestCase):
    def setUp(self):
        self.manager = TodoManager()

    def test_add_task_with_title_and_description(self):
        """Test adding a task with both title and description"""
        task_id = self.manager.add_task("Test Title", "Test Description")

        self.assertEqual(task_id, 1)
        self.assertEqual(len(self.manager.list_tasks()), 1)
        task = self.manager.list_tasks()[0]
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Title")
        self.assertEqual(task.description, "Test Description")
        self.assertFalse(task.completed)

    def test_add_task_with_title_only(self):
        """Test adding a task with only title"""
        task_id = self.manager.add_task("Test Title")

        self.assertEqual(task_id, 1)
        self.assertEqual(len(self.manager.list_tasks()), 1)
        task = self.manager.list_tasks()[0]
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Title")
        self.assertEqual(task.description, "")
        self.assertFalse(task.completed)

    def test_add_multiple_tasks_auto_increment(self):
        """Test that IDs are auto-incremented"""
        id1 = self.manager.add_task("First Task")
        id2 = self.manager.add_task("Second Task")
        id3 = self.manager.add_task("Third Task")

        self.assertEqual(id1, 1)
        self.assertEqual(id2, 2)
        self.assertEqual(id3, 3)

        tasks = self.manager.list_tasks()
        self.assertEqual(len(tasks), 3)
        self.assertEqual(tasks[0].id, 1)
        self.assertEqual(tasks[1].id, 2)
        self.assertEqual(tasks[2].id, 3)


if __name__ == '__main__':
    unittest.main()