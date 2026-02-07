"""
Unit tests for the list tasks functionality
"""
import unittest
from src.todo_manager import TodoManager


class TestListTasks(unittest.TestCase):
    def setUp(self):
        self.manager = TodoManager()

    def test_list_empty_tasks(self):
        """Test listing when there are no tasks"""
        tasks = self.manager.list_tasks()
        self.assertEqual(len(tasks), 0)

    def test_list_tasks_with_items(self):
        """Test listing tasks with multiple items"""
        # Add some tasks
        self.manager.add_task("First Task", "Description 1")
        self.manager.add_task("Second Task", "Description 2")
        self.manager.add_task("Third Task", "Description 3")

        tasks = self.manager.list_tasks()
        self.assertEqual(len(tasks), 3)
        self.assertEqual(tasks[0].title, "First Task")
        self.assertEqual(tasks[1].title, "Second Task")
        self.assertEqual(tasks[2].title, "Third Task")

    def test_list_tasks_after_deletion(self):
        """Test that list reflects deletions"""
        # Add tasks
        self.manager.add_task("Task 1")
        self.manager.add_task("Task 2")
        task3_id = self.manager.add_task("Task 3")

        # Delete one task
        self.manager.delete_task(task3_id)

        tasks = self.manager.list_tasks()
        self.assertEqual(len(tasks), 2)
        titles = [task.title for task in tasks]
        self.assertIn("Task 1", titles)
        self.assertIn("Task 2", titles)
        self.assertNotIn("Task 3", titles)

    def test_list_tasks_preserves_order(self):
        """Test that tasks are listed in the order they were added"""
        # Add tasks in specific order
        self.manager.add_task("Task A")
        self.manager.add_task("Task B")
        self.manager.add_task("Task C")

        tasks = self.manager.list_tasks()
        self.assertEqual(tasks[0].title, "Task A")
        self.assertEqual(tasks[1].title, "Task B")
        self.assertEqual(tasks[2].title, "Task C")


if __name__ == '__main__':
    unittest.main()