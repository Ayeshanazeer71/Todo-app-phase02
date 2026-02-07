# Data Model: Rich Todo Console Application

## Entity: Task

### Fields
- **id**: int (auto-incrementing, unique, required)
  - Auto-assigned starting from 1
  - Used as identifier for operations
- **title**: str (required, non-empty after validation)
  - User-defined title for the task
  - Minimum length: 1 character after whitespace stripping
- **description**: str (optional)
  - User-defined description for the task
  - Can be empty string if not provided
- **completed**: bool (required)
  - Status indicator for task completion
  - Default value: False

### Relationships
- None (standalone entity)

### Validation Rules
- id: Must be a positive integer, auto-incremented from the previous highest ID
- title: Must be a non-empty string after whitespace is stripped (length > 0)
- description: Can be any string (including empty)
- completed: Must be a boolean value

### State Transitions
- completed field can transition between True and False states
- id field is immutable after creation
- title and description fields can be updated after creation

## Entity: TaskList

### Fields
- **tasks**: List[Task] (collection of Task entities)
  - Internal representation of all tasks
  - Maintains order of creation

### Relationships
- Contains multiple Task entities

### Validation Rules
- All IDs must be unique within the list
- No duplicate IDs allowed
- Tasks can be added, updated, deleted, or have their status toggled