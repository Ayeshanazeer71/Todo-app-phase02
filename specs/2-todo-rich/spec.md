# Feature Specification: Rich Todo Console Application

**Feature Branch**: `2-todo-rich`
**Created**: 2025-12-31
**Status**: Draft
**Input**: User description: "Refine the specification to build a highly polished, professional-grade console Todo app using the rich library.

Detailed requirements and enhancements:

Core 5 features (must be perfect):
1. Add Task → Prompt for title and description (title required, description optional)
2. List/View Tasks → Display as a beautiful rich Table with columns:
   - ID (centered)
   - Status (✅ in green if complete, ❌ in red if incomplete)
   - Title (bold if complete)
   - Description (truncated to 50 chars with "..." if longer)
3. Update Task → By ID, then submenu: update title / description / both / cancel
4. Delete Task → By ID, with confirmation: "Are you sure you want to delete task X: 'Title'? (y/n)"
5. Mark as Complete/Incomplete → By ID, toggle status with success message

UI/UX Polish:
- App title in a rich Panel: "📝 My Todo App" (bold, cyan background)
- Below title: Live summary "Total: X tasks | Completed: Y | Pending: Z" (updated every loop)
- Main menu as numbered rich list inside a bordered panel
- All user prompts clean and guided (e.g., "Enter task title: ")
- Input validation:
  - Title cannot be empty (re-prompt if blank)
  - Strip whitespace
  - Invalid ID → red error: "Task with ID X not found!"
- Success messages in green, errors in red, info in yellow
- On exit: "Goodbye! 👋"

Technical:
- Use rich.console.Console, Table, Panel, Prompt
- Status emoji with color: live_style based on completed
- Keep code modular as per constitution
- Handle empty task list gracefully: show friendly message in table

Strictly NO extra features (no priority, due date, search, sort, etc.) — Phase I compliant only."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Add New Tasks (Priority: P1)

As a user, I want to add new tasks to my todo list so that I can keep track of things I need to do. When I select the "Add Task" option, I am prompted to enter a title and description for the task. The system validates that the title is not empty and strips whitespace. After I provide this information, the system assigns a unique ID and adds the task to my list with a default status of incomplete.

**Why this priority**: This is the foundational functionality that enables all other features - without the ability to add tasks, the application has no purpose.

**Independent Test**: Can be fully tested by adding multiple tasks with different titles and descriptions and verifying they appear in the task list with unique IDs and correct information.

**Acceptance Scenarios**:

1. **Given** I am using the todo application, **When** I select option 1 to add a task and provide a valid title and description, **Then** a new task with a unique ID is added to my list with status "Incomplete".
2. **Given** I have existing tasks in my list, **When** I add a new task, **Then** the new task gets the next sequential ID number.
3. **Given** I attempt to add a task with an empty title, **When** I submit the input, **Then** I am prompted again with an error message and the input is rejected.

---

### User Story 2 - View/List Tasks (Priority: P1)

As a user, I want to view all my tasks so that I can see what I need to do. When I select the "View/List Tasks" option, I see a beautiful rich table with columns for ID (centered), Status (✅ in green if complete, ❌ in red if incomplete), Title (bold if complete), and Description (truncated to 50 chars with "..." if longer). The table shows a live summary at the top: "Total: X tasks | Completed: Y | Pending: Z".

**Why this priority**: This is the primary way users interact with their tasks and is essential for the application's core purpose.

**Independent Test**: Can be fully tested by adding tasks and then viewing the list to verify all tasks display correctly with proper formatting and status indicators.

**Acceptance Scenarios**:

1. **Given** I have multiple tasks in my list, **When** I select option 2 to list tasks, **Then** all tasks are displayed in a rich table with proper formatting and color coding.
2. **Given** I have no tasks in my list, **When** I select option 2 to list tasks, **Then** a friendly message is displayed in the table indicating that there are no tasks available.

---

### User Story 3 - Update Task Information (Priority: P2)

As a user, I want to update the title and/or description of my tasks so that I can keep the information accurate. When I select the "Update Task" option and provide a valid task ID, I am presented with a submenu to update title, description, both, or cancel. After making my selection, I am prompted for the new information.

**Why this priority**: This allows users to maintain and refine their task information over time, improving the utility of the application.

**Independent Test**: Can be fully tested by updating existing tasks and verifying the changes are reflected when viewing the task list.

**Acceptance Scenarios**:

1. **Given** I have a task in my list, **When** I select option 3 to update a task and provide a valid ID along with new information, **Then** the task details are updated accordingly.
2. **Given** I try to update a task with an invalid ID, **When** I enter the ID, **Then** a red error message "Task with ID X not found!" is displayed.

---

### User Story 4 - Delete Tasks (Priority: P2)

As a user, I want to delete tasks from my list so that I can remove items I no longer need. When I select the "Delete Task" option and provide a valid task ID, I am prompted for confirmation with the message "Are you sure you want to delete task X: 'Title'? (y/n)". If I confirm, the task is removed from my list.

**Why this priority**: This allows users to clean up their task list and maintain only relevant items.

**Independent Test**: Can be fully tested by deleting tasks and verifying they no longer appear in the task list.

**Acceptance Scenarios**:

1. **Given** I have a task in my list, **When** I select option 4 to delete a task and provide a valid ID and confirm deletion, **Then** the task is removed from the list.
2. **Given** I try to delete a task with an invalid ID, **When** I enter the ID, **Then** a red error message "Task with ID X not found!" is displayed.

---

### User Story 5 - Mark Tasks Complete/Incomplete (Priority: P2)

As a user, I want to mark tasks as complete or incomplete so that I can track my progress. When I select the "Mark Complete/Incomplete" option and provide a valid task ID, the completion status of that task is toggled and a success message is displayed in green.

**Why this priority**: This is essential for tracking task completion, which is a core function of a todo application.

**Independent Test**: Can be fully tested by toggling task completion status and verifying the status updates correctly when viewing the task list.

**Acceptance Scenarios**:

1. **Given** I have an incomplete task in my list, **When** I select option 5 and provide the task ID, **Then** the task's status changes to "Complete" and a success message is shown.
2. **Given** I have a completed task in my list, **When** I select option 5 and provide the task ID, **Then** the task's status changes to "Incomplete" and a success message is shown.

---

### User Story 6 - Navigate Rich Menu System (Priority: P1)

As a user, I want a beautiful, polished menu system so that I can easily navigate between different functions of the application. The application displays a rich panel with the title "📝 My Todo App" (bold, cyan background) and a live summary below: "Total: X tasks | Completed: Y | Pending: Z". The main menu appears as a numbered rich list inside a bordered panel.

**Why this priority**: This is the primary interface for all other functionality and is essential for the professional-grade user experience.

**Independent Test**: Can be fully tested by navigating through all menu options and verifying each function works as expected with proper rich formatting.

**Acceptance Scenarios**:

1. **Given** I am in the main menu, **When** I enter a valid menu option number, **Then** the corresponding function is executed with proper rich formatting.
2. **Given** I am in the main menu, **When** I enter an invalid menu option, **Then** a red error message is displayed and the menu is shown again with rich formatting.

---

### Edge Cases

- What happens when a user tries to update/delete/mark a task that doesn't exist? (System should display "Task with ID X not found!" in red)
- How does the system handle empty input when adding tasks? (System should re-prompt with error message)
- What happens when a user enters non-numeric input when an ID is expected? (System should handle gracefully with red error message)
- How does the system behave when the task list is empty during view operations? (System should display friendly message in table)
- What happens when description is longer than 50 characters? (System should truncate with "..." indicator)

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST provide a rich menu-driven console interface with numbered options (1.Add, 2.List, 3.Update, 4.Delete, 5.Mark Complete, 6.Exit) displayed in a bordered panel
- **FR-002**: System MUST allow users to add tasks with a title (required) and description (optional)
- **FR-003**: System MUST validate that task titles cannot be empty and strip whitespace
- **FR-004**: System MUST assign unique, auto-incrementing IDs starting from 1 to each new task
- **FR-005**: System MUST display all tasks in a beautiful rich table with ID (centered), Status (✅ in green if complete, ❌ in red if incomplete), Title (bold if complete), and Description (truncated to 50 chars with "..." if longer)
- **FR-006**: System MUST display a rich panel with title "📝 My Todo App" (bold, cyan background) and live summary "Total: X tasks | Completed: Y | Pending: Z"
- **FR-007**: System MUST allow users to update task title and/or description by providing the task ID and selecting from submenu options (update title / description / both / cancel)
- **FR-008**: System MUST allow users to delete tasks by providing the task ID with confirmation prompt "Are you sure you want to delete task X: 'Title'? (y/n)"
- **FR-009**: System MUST allow users to toggle the completion status of tasks by providing the task ID
- **FR-010**: System MUST handle invalid inputs gracefully with appropriate colored error messages (red for errors, green for success, yellow for info)
- **FR-011**: System MUST use the rich library for all console UI elements including tables, panels, colors, and emojis
- **FR-012**: System MUST handle empty task list gracefully by showing a friendly message in the table

### Key Entities *(include if feature involves data)*

- **Task**: Represents a single todo item with attributes: id (auto-incrementing integer), title (string), description (string), completed (boolean with default False)
- **Task List**: Collection of Task entities stored in memory during application runtime

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can add, view, update, delete, and mark tasks as complete within a single session with 100% success rate and rich formatting
- **SC-002**: All user actions result in appropriate colored feedback with no application crashes during normal usage
- **SC-003**: Users can successfully navigate the rich menu system and execute all functions without confusion
- **SC-004**: Error handling prevents application crashes with invalid inputs and provides clear colored error messages
- **SC-005**: Application provides professional-grade console experience with rich tables, panels, colors, and emojis