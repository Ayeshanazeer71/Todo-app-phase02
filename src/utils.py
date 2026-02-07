"""
Utility functions for the Todo Console Application
Helper functions for input validation, formatting, etc.
"""
from typing import List, Optional
from .models import Task


def format_task_status(completed: bool) -> str:
    """
    Format the completion status as an ASCII indicator
    """
    return "[Complete]" if completed else "[Incomplete]"


def display_task(task: Task) -> str:
    """
    Format a single task for display
    """
    status = format_task_status(task.completed)
    return f"ID: {task.id} | Title: {task.title} | Description: {task.description} | Status: {status}"


def display_tasks(tasks: List[Task]) -> str:
    """
    Format a list of tasks for display
    """
    if not tasks:
        return "No tasks available."

    task_list = []
    for task in tasks:
        status = format_task_status(task.completed)
        task_list.append(f"{task.id}. {task.title} - {status}")

    return "\n".join(task_list)


def display_tasks_detailed(tasks: List[Task]) -> str:
    """
    Format a list of tasks for detailed display
    """
    if not tasks:
        return "No tasks available."

    task_list = []
    for task in tasks:
        status = format_task_status(task.completed)
        task_info = f"ID: {task.id}\nTitle: {task.title}\nDescription: {task.description}\nStatus: {status}\n"
        task_list.append(task_info)

    return "\n".join(task_list)


def validate_task_input(title: str, description: str = "") -> Optional[str]:
    """
    Validate task input and return error message if invalid
    """
    if not title or not title.strip():
        return "Title cannot be empty"
    if len(title.strip()) == 0:
        return "Title cannot be empty"

    return None


def validate_task_id(task_id: str) -> Optional[int]:
    """
    Validate that the provided task ID is a valid integer
    Returns the integer ID if valid, None if invalid
    """
    try:
        id_num = int(task_id)
        if id_num <= 0:
            return None
        return id_num
    except ValueError:
        return None


def get_user_choice() -> Optional[int]:
    """
    Get and validate user menu choice
    """
    choice = input("\nEnter your choice: ").strip()
    try:
        return int(choice)
    except ValueError:
        return None


def display_menu() -> None:
    """
    Display the main menu
    """
    print("\n" + "="*40)
    print("TODO CONSOLE APPLICATION")
    print("="*40)
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Complete/Incomplete")
    print("6. Exit")
    print("="*40)


def safe_input(prompt: str) -> str:
    """
    Get user input safely
    """
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        print("\nOperation cancelled.")
        return ""