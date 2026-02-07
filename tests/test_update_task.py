"""
Unit tests for the update task functionality
"""
import unittest
from src.todo_manager import TodoManager


class TestUpdateTask(unittest.TestCase):
    def setUp(self):
        self.manager = TodoManager()

    def test_update_task_title_only(self):
        """Test updating only the title of a task"""
        task_id = self.manager.add_task("Original Title", "Original Description")

        success = self.manager.update_task(task_id, title="Updated Title")

        self.assertTrue(success)
        task = self.manager.get_task_by_id(task_id)
        self.assertEqual(task.title, "Updated Title")
        self.assertEqual(task.description, "Original Description")
        self.assertFalse(task.completed)

    def test_update_task_description_only(self):
        """Test updating only the description of a task"""
        task_id = self.manager.add_task("Original Title", "Original Description")

        success = self.manager.update_task(task_id, description="Updated Description")

        self.assertTrue(success)
        task = self.manager.get_task_by_id(task_id)
        self.assertEqual(task.title, "Original Title")
        self.assertEqual(task.description, "Updated Description")
        self.assertFalse(task.completed)

    def test_update_task_both_fields(self):
        """Test updating both title and description of a task"""
        task_id = self.manager.add_task("Original Title", "Original Description")

        success = self.manager.update_task(task_id, title="Updated Title", description="Updated Description")

        self.assertTrue(success)
        task = self.manager.get_task_by_id(task_id)
        self.assertEqual(task.title, "Updated Title")
        self.assertEqual(task.description, "Updated Description")
        self.assertFalse(task.completed)

    def test_update_nonexistent_task(self):
        """Test updating a task that doesn't exist"""
        success = self.manager.update_task(999, title="Updated Title")

        self.assertFalse(success)

    def test_update_task_to_completed_state(self):
        """Test that updating doesn't change completion status"""
        task_id = self.manager.add_task("Original Title", "Original Description")
        # Mark as completed first
        self.manager.toggle_task_status(task_id)

        success = self.manager.update_task(task_id, title="Updated Title")

        self.assertTrue(success)
        task = self.manager.get_task_by_id(task_id)
        self.assertEqual(task.title, "Updated Title")
        self.assertTrue(task.completed)  # Should remain completed


if __name__ == '__main__':
    unittest.main()