"""
Main module for the Rich Todo Console Application
Entry point with menu loop only
"""
from typing import Optional
from operations import TaskOperations
from ui import UIHandler


class TodoApp:
    """
    Main application class that handles the menu system and user interactions
    """
    def __init__(self):
        self.operations = TaskOperations()
        self.ui = UIHandler()

    def run(self):
        """
        Main application loop that displays menu and processes user input
        """
        self.ui.display_app_title()

        while True:
            # Update and display task summary
            tasks = self.operations.list_tasks()
            self.ui.display_task_summary(tasks)

            # Display menu and get user choice
            self.ui.display_menu()
            choice = self.ui.get_user_choice()

            if choice == 1:
                self.add_task()
            elif choice == 2:
                self.list_tasks()
            elif choice == 3:
                self.update_task()
            elif choice == 4:
                self.delete_task()
            elif choice == 5:
                self.toggle_task_status()
            elif choice == 6:
                self.ui.show_exit_message()
                break
            else:
                self.ui.show_error("Invalid choice. Please enter a number between 1-6.")

    def add_task(self):
        """
        Handle adding a new task
        """
        title, description = self.ui.get_task_input()
        task_id = self.operations.add_task(title, description)
        self.ui.show_success(f"Task added successfully with ID: {task_id}")

    def list_tasks(self):
        """
        Handle listing all tasks
        """
        tasks = self.operations.list_tasks()
        self.ui.display_tasks_table(tasks)

    def update_task(self):
        """
        Handle updating an existing task
        """
        task_id = self.ui.get_task_id()
        if task_id is None:
            return

        task = self.operations.get_task_by_id(task_id)
        if task is None:
            self.ui.show_error(f"Task with ID {task_id} not found!")
            return

        # Get update option from user
        option = self.ui.get_update_options()

        if option == "4":  # Cancel
            self.ui.show_info("Update cancelled.")
            return

        if option == "1":  # Update title only
            new_title = self.ui.get_task_input()[0]  # Get only title
            success = self.operations.update_task(task_id, title=new_title)
        elif option == "2":  # Update description only
            current_task = self.operations.get_task_by_id(task_id)
            if current_task:
                new_description = self.ui.get_task_input()[1]  # Get only description
                success = self.operations.update_task(task_id, description=new_description)
            else:
                success = False
        elif option == "3":  # Update both
            new_title, new_description = self.ui.get_task_input()
            success = self.operations.update_task(task_id, title=new_title, description=new_description)
        else:
            success = False

        if success:
            self.ui.show_success("Task updated successfully.")
        else:
            self.ui.show_error("Failed to update task.")

    def delete_task(self):
        """
        Handle deleting a task
        """
        task_id = self.ui.get_task_id()
        if task_id is None:
            return

        task = self.operations.get_task_by_id(task_id)
        if task is None:
            self.ui.show_error(f"Task with ID {task_id} not found!")
            return

        if self.ui.confirm_delete(task):
            success = self.operations.delete_task(task_id)
            if success:
                self.ui.show_success("Task deleted successfully.")
            else:
                self.ui.show_error("Failed to delete task.")
        else:
            self.ui.show_info("Deletion cancelled.")

    def toggle_task_status(self):
        """
        Handle toggling task completion status
        """
        task_id = self.ui.get_task_id()
        if task_id is None:
            return

        task = self.operations.get_task_by_id(task_id)
        if task is None:
            self.ui.show_error(f"Task with ID {task_id} not found!")
            return

        success = self.operations.toggle_task_status(task_id)
        if success:
            new_status = "Complete" if task.completed else "Incomplete"
            self.ui.show_success(f"Task status updated to: {new_status}")
        else:
            self.ui.show_error("Failed to toggle task status.")


def main():
    """
    Entry point for the application
    """
    try:
        app = TodoApp()
        app.run()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("Please restart the application.")


if __name__ == "__main__":
    main()