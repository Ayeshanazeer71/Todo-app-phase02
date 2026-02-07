# Quickstart: Todo Console Application

## Prerequisites
- Python 3.13 or higher
- No external dependencies required (pure standard library)

## Setup
1. Clone the repository
2. Navigate to the project directory
3. Run the application: `python -m src.main`

## Running the Application
```bash
python -m src.main
```

## Usage
Once the application starts, you'll see a menu with the following options:
1. Add Task
2. List Tasks
3. Update Task
4. Delete Task
5. Mark Complete/Incomplete
6. Exit

Follow the on-screen prompts to interact with your todo list.

## Development
To run tests:
```bash
python -m unittest discover tests
```

## Project Structure
- `src/main.py`: Main application entry point with menu loop
- `src/models.py`: Task dataclass definition
- `src/todo_manager.py`: Core business logic for task operations
- `src/utils.py`: Helper functions for input validation and formatting
- `tests/`: Unit and integration tests