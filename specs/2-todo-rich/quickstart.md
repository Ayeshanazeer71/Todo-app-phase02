# Quickstart: Rich Todo Console Application

## Prerequisites
- Python 3.13 or higher
- Rich library: `pip install rich`

## Setup
1. Clone the repository
2. Navigate to the project directory
3. Install dependencies: `pip install rich`
4. Run the application: `python -m src.main`

## Running the Application
```bash
python -m src.main
```

## Usage
Once the application starts, you'll see a rich menu with the following options:
1. Add Task
2. List Tasks
3. Update Task
4. Delete Task
5. Mark Complete/Incomplete
6. Exit

Follow the on-screen prompts to interact with your todo list. The application features:
- Rich panel with title "📝 My Todo App" (bold, cyan background)
- Live summary "Total: X tasks | Completed: Y | Pending: Z"
- Beautiful rich table for displaying tasks
- Colored messages (green for success, red for errors, yellow for info)

## Development
To run tests:
```bash
python -m unittest discover tests
```

## Project Structure
- `src/main.py`: Main application entry point with menu loop
- `src/models.py`: Task dataclass definition
- `src/operations.py`: Core business logic for task operations (CRUD functions)
- `src/ui.py`: All display, menu, prompts, and rich formatting
- `tests/`: Unit and integration tests