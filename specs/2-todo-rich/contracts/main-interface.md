# Interface Contract: Rich Todo Console Application

## Main Application Interface

### Entry Point
- Module: `src.main`
- Function: `main()` - Entry point for the application
- Expected behavior: Initializes the application and starts the rich menu loop

### Core Functions

#### Task Management Functions (in operations.py)
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

#### UI Display Functions (in ui.py)
- `display_menu(console: Console) -> None`
  - Input: Rich Console instance
  - Output: Displays the main menu to console using rich panels
  - Behavior: Shows numbered options in a bordered panel

- `display_task_summary(console: Console, tasks: List[Task]) -> None`
  - Input: Rich Console instance, list of tasks
  - Output: Displays live summary in rich format
  - Behavior: Shows "Total: X tasks | Completed: Y | Pending: Z"

- `display_tasks_table(console: Console, tasks: List[Task]) -> None`
  - Input: Rich Console instance, list of tasks
  - Output: Displays tasks in a rich table
  - Behavior: Shows tasks with ID (centered), Status (✅ in green if complete, ❌ in red if incomplete), Title (bold if complete), and Description (truncated to 50 chars with "..." if longer)

- `get_user_choice(console: Console) -> Optional[int]`
  - Input: Rich Console instance
  - Output: User's menu choice as integer
  - Behavior: Prompts user and validates input

#### Input/Output Functions (in ui.py)
- `get_task_input(console: Console) -> Tuple[str, str]`
  - Input: Rich Console instance
  - Output: Tuple of (title, description) from user
  - Behavior: Prompts user for task title and description with validation

- `show_error(console: Console, message: str) -> None`
  - Input: Rich Console instance, error message
  - Output: Displays error message in red
  - Behavior: Shows error message in red color

- `show_success(console: Console, message: str) -> None`
  - Input: Rich Console instance, success message
  - Output: Displays success message in green
  - Behavior: Shows success message in green color

- `show_info(console: Console, message: str) -> None`
  - Input: Rich Console instance, info message
  - Output: Displays info message in yellow
  - Behavior: Shows info message in yellow color