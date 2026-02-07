"""
Unit tests for the Rich Todo Console Application
"""
import unittest
from src.operations import TaskOperations
from src.models import Task


class TestRichTodo(unittest.TestCase):
    def setUp(self):
        self.operations = TaskOperations()

    def test_add_task(self):
        """Test adding a task"""
        task_id = self.operations.add_task("Test Task", "Test Description")

        self.assertEqual(task_id, 1)
        tasks = self.operations.list_tasks()
        self.assertEqual(len(tasks), 1)
        task = tasks[0]
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")
        self.assertFalse(task.completed)

    def test_list_tasks(self):
        """Test listing tasks"""
        # Add some tasks
        self.operations.add_task("Task 1", "Description 1")
        self.operations.add_task("Task 2", "Description 2")

        tasks = self.operations.list_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].title, "Task 1")
        self.assertEqual(tasks[1].title, "Task 2")

    def test_get_task_by_id(self):
        """Test getting a task by ID"""
        task_id = self.operations.add_task("Test Task", "Description")

        task = self.operations.get_task_by_id(task_id)
        self.assertIsNotNone(task)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Description")

    def test_get_task_by_id_not_found(self):
        """Test getting a task that doesn't exist"""
        task = self.operations.get_task_by_id(999)
        self.assertIsNone(task)

    def test_update_task_title(self):
        """Test updating task title"""
        task_id = self.operations.add_task("Original Title", "Original Description")

        success = self.operations.update_task(task_id, title="Updated Title")

        self.assertTrue(success)
        task = self.operations.get_task_by_id(task_id)
        self.assertEqual(task.title, "Updated Title")
        self.assertEqual(task.description, "Original Description")

    def test_update_task_description(self):
        """Test updating task description"""
        task_id = self.operations.add_task("Original Title", "Original Description")

        success = self.operations.update_task(task_id, description="Updated Description")

        self.assertTrue(success)
        task = self.operations.get_task_by_id(task_id)
        self.assertEqual(task.title, "Original Title")
        self.assertEqual(task.description, "Updated Description")

    def test_update_task_both(self):
        """Test updating both title and description"""
        task_id = self.operations.add_task("Original Title", "Original Description")

        success = self.operations.update_task(task_id, title="Updated Title", description="Updated Description")

        self.assertTrue(success)
        task = self.operations.get_task_by_id(task_id)
        self.assertEqual(task.title, "Updated Title")
        self.assertEqual(task.description, "Updated Description")

    def test_delete_task(self):
        """Test deleting a task"""
        task_id = self.operations.add_task("Task to Delete", "Description")

        success = self.operations.delete_task(task_id)

        self.assertTrue(success)
        tasks = self.operations.list_tasks()
        self.assertEqual(len(tasks), 0)

    def test_delete_task_not_found(self):
        """Test deleting a task that doesn't exist"""
        success = self.operations.delete_task(999)

        self.assertFalse(success)

    def test_toggle_task_status(self):
        """Test toggling task status"""
        task_id = self.operations.add_task("Test Task", "Description")

        # Initially should be incomplete
        task = self.operations.get_task_by_id(task_id)
        self.assertFalse(task.completed)

        # Toggle to complete
        success = self.operations.toggle_task_status(task_id)

        self.assertTrue(success)
        task = self.operations.get_task_by_id(task_id)
        self.assertTrue(task.completed)

        # Toggle back to incomplete
        success = self.operations.toggle_task_status(task_id)

        self.assertTrue(success)
        task = self.operations.get_task_by_id(task_id)
        self.assertFalse(task.completed)

    def test_auto_incrementing_ids(self):
        """Test that IDs are auto-incremented"""
        id1 = self.operations.add_task("Task 1")
        id2 = self.operations.add_task("Task 2")
        id3 = self.operations.add_task("Task 3")

        self.assertEqual(id1, 1)
        self.assertEqual(id2, 2)
        self.assertEqual(id3, 3)


if __name__ == '__main__':
    unittest.main()