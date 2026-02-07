"""
Integration tests for the main application flow
"""
import unittest
from unittest.mock import patch, MagicMock
from src.main import TodoApp
from src.todo_manager import TodoManager


class TestMainApp(unittest.TestCase):
    def setUp(self):
        self.app = TodoApp()

    @patch('src.main.safe_input')
    @patch('src.main.get_user_choice')
    def test_add_task_flow(self, mock_get_choice, mock_safe_input):
        """Test the add task flow through the main app"""
        # Simulate user inputs
        mock_get_choice.return_value = 1  # Add task option
        mock_safe_input.side_effect = ["Test Title", "Test Description"]

        # Capture the current task count
        initial_count = len(self.app.manager.list_tasks())

        # Execute the add task flow
        self.app.add_task()

        # Verify task was added
        final_count = len(self.app.manager.list_tasks())
        self.assertEqual(final_count, initial_count + 1)
        task = self.app.manager.list_tasks()[-1]
        self.assertEqual(task.title, "Test Title")
        self.assertEqual(task.description, "Test Description")

    @patch('src.main.safe_input')
    @patch('src.main.get_user_choice')
    def test_list_tasks_flow(self, mock_get_choice, mock_safe_input):
        """Test the list tasks flow through the main app"""
        # Add a task first
        self.app.manager.add_task("Test Task", "Test Description")

        # Set up mocks
        mock_get_choice.return_value = 2  # List tasks option
        mock_safe_input.return_value = ""  # No input needed for listing

        # Execute the list tasks flow
        self.app.list_tasks()

        # Verify tasks exist
        tasks = self.app.manager.list_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].title, "Test Task")

    @patch('src.main.safe_input')
    @patch('src.main.get_user_choice')
    def test_update_task_flow(self, mock_get_choice, mock_safe_input):
        """Test the update task flow through the main app"""
        # Add a task first
        task_id = self.app.manager.add_task("Original Title", "Original Description")

        # Set up mocks for update flow
        mock_get_choice.return_value = 3  # Update task option
        mock_safe_input.side_effect = [
            str(task_id),  # Task ID
            "Updated Title",  # New title
            "Updated Description"  # New description
        ]

        # Execute the update task flow
        self.app.update_task()

        # Verify task was updated
        task = self.app.manager.get_task_by_id(task_id)
        self.assertEqual(task.title, "Updated Title")
        self.assertEqual(task.description, "Updated Description")

    @patch('src.main.safe_input')
    @patch('src.main.get_user_choice')
    def test_delete_task_flow(self, mock_get_choice, mock_safe_input):
        """Test the delete task flow through the main app"""
        # Add a task first
        task_id = self.app.manager.add_task("Task to Delete", "Description")

        # Set up mocks for delete flow
        mock_get_choice.return_value = 4  # Delete task option
        mock_safe_input.side_effect = [
            str(task_id),  # Task ID
            "y"  # Confirm deletion
        ]

        # Execute the delete task flow
        self.app.delete_task()

        # Verify task was deleted
        task = self.app.manager.get_task_by_id(task_id)
        self.assertIsNone(task)

    @patch('src.main.safe_input')
    @patch('src.main.get_user_choice')
    def test_toggle_task_status_flow(self, mock_get_choice, mock_safe_input):
        """Test the toggle task status flow through the main app"""
        # Add a task first
        task_id = self.app.manager.add_task("Test Task", "Description")

        # Set up mocks for toggle flow
        mock_get_choice.return_value = 5  # Toggle status option
        mock_safe_input.return_value = str(task_id)  # Task ID

        # Execute the toggle task status flow
        self.app.toggle_task_status()

        # Verify status was toggled
        task = self.app.manager.get_task_by_id(task_id)
        self.assertTrue(task.completed)  # Should now be complete


if __name__ == '__main__':
    unittest.main()