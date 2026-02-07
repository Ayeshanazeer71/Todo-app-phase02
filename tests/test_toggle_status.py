"""
Unit tests for the toggle task status functionality
"""
import unittest
from src.todo_manager import TodoManager


class TestToggleStatus(unittest.TestCase):
    def setUp(self):
        self.manager = TodoManager()

    def test_toggle_task_from_incomplete_to_complete(self):
        """Test toggling a task from incomplete to complete"""
        task_id = self.manager.add_task("Test Task", "Description")

        # Initially should be incomplete
        task = self.manager.get_task_by_id(task_id)
        self.assertFalse(task.completed)

        # Toggle to complete
        success = self.manager.toggle_task_status(task_id)

        self.assertTrue(success)
        task = self.manager.get_task_by_id(task_id)
        self.assertTrue(task.completed)

    def test_toggle_task_from_complete_to_incomplete(self):
        """Test toggling a task from complete to incomplete"""
        task_id = self.manager.add_task("Test Task", "Description")

        # First toggle to complete
        self.manager.toggle_task_status(task_id)
        task = self.manager.get_task_by_id(task_id)
        self.assertTrue(task.completed)

        # Then toggle back to incomplete
        success = self.manager.toggle_task_status(task_id)

        self.assertTrue(success)
        task = self.manager.get_task_by_id(task_id)
        self.assertFalse(task.completed)

    def test_toggle_nonexistent_task(self):
        """Test toggling a task that doesn't exist"""
        success = self.manager.toggle_task_status(999)

        self.assertFalse(success)

    def test_toggle_multiple_tasks(self):
        """Test toggling status of multiple tasks"""
        task1_id = self.manager.add_task("Task 1")
        task2_id = self.manager.add_task("Task 2")
        task3_id = self.manager.add_task("Task 3")

        # Toggle first task to complete
        self.manager.toggle_task_status(task1_id)

        # Verify only task 1 is complete
        task1 = self.manager.get_task_by_id(task1_id)
        task2 = self.manager.get_task_by_id(task2_id)
        task3 = self.manager.get_task_by_id(task3_id)

        self.assertTrue(task1.completed)
        self.assertFalse(task2.completed)
        self.assertFalse(task3.completed)

        # Toggle task 2 to complete
        self.manager.toggle_task_status(task2_id)

        # Verify task 1 and 2 are complete, task 3 is incomplete
        task1 = self.manager.get_task_by_id(task1_id)
        task2 = self.manager.get_task_by_id(task2_id)
        task3 = self.manager.get_task_by_id(task3_id)

        self.assertTrue(task1.completed)
        self.assertTrue(task2.completed)
        self.assertFalse(task3.completed)


if __name__ == '__main__':
    unittest.main()