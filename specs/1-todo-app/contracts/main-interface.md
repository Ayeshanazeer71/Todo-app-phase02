# Interface Contract: Todo Console Application

## Main Application Interface

### Entry Point
- Module: `src.main`
- Function: `main()` - Entry point for the application
- Expected behavior: Initializes the application and starts the menu loop

### Core Functions

#### Task Management Functions
- `add_task(title: str, description: str = "") -> int`
  - Input: Task title (required), description (optional)
  - Output: Assigned task ID
  - Behavior: Creates new task with auto-incremented ID and returns the ID

- `list_tasks() -> List[Task]`
  - Input: None
  - Output: List of all tasks in the system
  - Behavior: Returns all tasks in the current session

- `update_task(task_id: int, title: str = None, description: str = None) -> bool`
  - Input: Task ID, optional new title, optional new description
  - Output: Boolean indicating success/failure
  - Behavior: Updates specified fields of a task, returns False if task doesn't exist

- `delete_task(task_id: int) -> bool`
  - Input: Task ID
  - Output: Boolean indicating success/failure
  - Behavior: Removes task from the system, returns False if task doesn't exist

- `toggle_task_status(task_id: int) -> bool`
  - Input: Task ID
  - Output: Boolean indicating success/failure
  - Behavior: Toggles the completed status of a task, returns False if task doesn't exist

#### Menu Interface Functions
- `display_menu() -> None`
  - Input: None
  - Output: Displays the main menu to console
  - Behavior: Shows numbered options to user

- `get_user_choice() -> int`
  - Input: None (reads from stdin)
  - Output: User's menu choice as integer
  - Behavior: Prompts user and validates input

#### Input/Output Functions
- `get_task_input() -> Tuple[str, str]`
  - Input: None (reads from stdin)
  - Output: Tuple of (title, description) from user
  - Behavior: Prompts user for task title and description

- `display_tasks(tasks: List[Task]) -> None`
  - Input: List of tasks to display
  - Output: Formatted display to console
  - Behavior: Shows tasks with ID, title, description, and status (✅/❌)