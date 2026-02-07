"""
Unit tests for the delete task functionality
"""
import unittest
from src.todo_manager import TodoManager


class TestDeleteTask(unittest.TestCase):
    def setUp(self):
        self.manager = TodoManager()

    def test_delete_existing_task(self):
        """Test deleting an existing task"""
        task_id = self.manager.add_task("Task to Delete", "Description")
        initial_count = len(self.manager.list_tasks())

        success = self.manager.delete_task(task_id)

        self.assertTrue(success)
        self.assertEqual(len(self.manager.list_tasks()), initial_count - 1)
        # Verify the task is no longer accessible
        self.assertIsNone(self.manager.get_task_by_id(task_id))

    def test_delete_nonexistent_task(self):
        """Test deleting a task that doesn't exist"""
        success = self.manager.delete_task(999)

        self.assertFalse(success)

    def test_delete_task_from_multiple_tasks(self):
        """Test deleting one task from multiple tasks"""
        task1_id = self.manager.add_task("Task 1", "Description 1")
        task2_id = self.manager.add_task("Task 2", "Description 2")
        task3_id = self.manager.add_task("Task 3", "Description 3")
        initial_count = len(self.manager.list_tasks())

        success = self.manager.delete_task(task2_id)

        self.assertTrue(success)
        self.assertEqual(len(self.manager.list_tasks()), initial_count - 1)

        # Verify other tasks still exist
        self.assertIsNotNone(self.manager.get_task_by_id(task1_id))
        self.assertIsNone(self.manager.get_task_by_id(task2_id))
        self.assertIsNotNone(self.manager.get_task_by_id(task3_id))

    def test_delete_all_tasks(self):
        """Test deleting all tasks one by one"""
        task1_id = self.manager.add_task("Task 1")
        task2_id = self.manager.add_task("Task 2")
        task3_id = self.manager.add_task("Task 3")

        self.manager.delete_task(task1_id)
        self.assertEqual(len(self.manager.list_tasks()), 2)

        self.manager.delete_task(task2_id)
        self.assertEqual(len(self.manager.list_tasks()), 1)

        self.manager.delete_task(task3_id)
        self.assertEqual(len(self.manager.list_tasks()), 0)


if __name__ == '__main__':
    unittest.main()