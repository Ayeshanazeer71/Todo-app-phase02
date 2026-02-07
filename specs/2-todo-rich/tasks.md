---
description: "Task list for Rich Todo Console Application implementation"
---

# Tasks: Rich Todo Console Application

**Input**: Design documents from `/specs/2-todo-rich/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure with src/ and tests/ directories
- [ ] T002 [P] Create src/__init__.py
- [ ] T003 [P] Create tests/__init__.py
- [ ] T004 Install rich library dependency

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T005 Create Task dataclass in src/models.py
- [ ] T006 Create operations module in src/operations.py
- [ ] T007 Create UI module in src/ui.py
- [ ] T008 Create main module in src/main.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new tasks to their todo list with a title and description, assigning unique IDs

**Independent Test**: Can add multiple tasks with different titles and descriptions and verify they appear in the task list with unique IDs and correct information

### Implementation for User Story 1

- [ ] T009 [P] [US1] Implement Task dataclass with id, title, description, completed attributes in src/models.py
- [ ] T010 [P] [US1] Create add_task method in operations module in src/operations.py
- [ ] T011 [US1] Implement auto-incrementing ID functionality in operations module
- [ ] T012 [US1] Create input validation for add_task in src/ui.py
- [ ] T013 [US1] Add error handling for empty title in src/ui.py
- [ ] T014 [US1] Implement rich console input for task title in src/ui.py
- [ ] T015 [US1] Test adding tasks with valid inputs

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View/List Tasks (Priority: P1)

**Goal**: Enable users to view all tasks with their ID, title, description, and completion status (✅ in green if complete, ❌ in red if incomplete) in a beautiful rich table

**Independent Test**: Can add tasks and then view the list to verify all tasks display correctly with proper formatting and status indicators

### Implementation for User Story 2

- [ ] T016 [P] [US2] Implement list_tasks method in operations module in src/operations.py
- [ ] T017 [P] [US2] Create rich table display function in src/ui.py
- [ ] T018 [US2] Add empty list handling in src/ui.py
- [ ] T019 [US2] Implement status indicators (✅/❌) with color coding for completion status
- [ ] T020 [US2] Implement title formatting (bold if complete) in rich table
- [ ] T021 [US2] Implement description truncation (to 50 chars with "...") in rich table
- [ ] T022 [US2] Test listing tasks with various completion states

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Task Information (Priority: P2)

**Goal**: Enable users to update the title and/or description of existing tasks by providing a valid task ID, with submenu options for update title/description/both/cancel

**Independent Test**: Can update existing tasks and verify the changes are reflected when viewing the task list

### Implementation for User Story 3

- [ ] T023 [P] [US3] Implement update_task method in operations module in src/operations.py
- [ ] T024 [P] [US3] Create input validation for update_task in src/ui.py
- [ ] T025 [US3] Add error handling for invalid task ID in src/ui.py
- [ ] T026 [US3] Implement submenu for update options (title/description/both/cancel) in src/ui.py
- [ ] T027 [US3] Implement partial updates (title only, description only, or both)
- [ ] T028 [US3] Test updating tasks with valid and invalid IDs

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Delete Tasks (Priority: P2)

**Goal**: Enable users to delete tasks from their list by providing a valid task ID, with confirmation prompt

**Independent Test**: Can delete tasks and verify they no longer appear in the task list

### Implementation for User Story 4

- [ ] T029 [P] [US4] Implement delete_task method in operations module in src/operations.py
- [ ] T030 [P] [US4] Add error handling for invalid task ID in src/ui.py
- [ ] T031 [US4] Implement confirmation prompt with rich formatting in src/ui.py
- [ ] T032 [US4] Implement confirmation message "Are you sure you want to delete task X: 'Title'? (y/n)" in src/ui.py
- [ ] T033 [US4] Test deleting tasks with valid and invalid IDs

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Mark Tasks Complete/Incomplete (Priority: P2)

**Goal**: Enable users to toggle the completion status of tasks by providing a valid task ID

**Independent Test**: Can toggle task completion status and verify the status updates correctly when viewing the task list

### Implementation for User Story 5

- [ ] T034 [P] [US5] Implement toggle_task_status method in operations module in src/operations.py
- [ ] T035 [P] [US5] Add error handling for invalid task ID in src/ui.py
- [ ] T036 [US5] Implement success message display in src/ui.py
- [ ] T037 [US5] Test toggling completion status of tasks

**Checkpoint**: At this point, all user stories should be independently functional

---

## Phase 8: User Story 6 - Navigate Rich Menu System (Priority: P1)

**Goal**: Provide a rich menu system with numbered options (1.Add, 2.List, 3.Update, 4.Delete, 5.Mark Complete, 6.Exit) inside a bordered panel, with app title panel and live summary

**Independent Test**: Can navigate through all menu options and verify each function works as expected

### Implementation for User Story 6

- [ ] T038 [P] [US6] Create rich menu display function in src/ui.py
- [ ] T039 [P] [US6] Create app title panel "📝 My Todo App" (bold, cyan background) in src/ui.py
- [ ] T040 [US6] Create live summary display "Total: X tasks | Completed: Y | Pending: Z" in src/ui.py
- [ ] T041 [US6] Create main application loop in src/main.py
- [ ] T042 [US6] Integrate all user story functions into main menu
- [ ] T043 [US6] Add menu option validation and error handling with rich formatting
- [ ] T044 [US6] Implement exit message "Goodbye! 👋" in src/ui.py
- [ ] T045 [US6] Test complete menu flow with all options

**Checkpoint**: All user stories now integrated into a complete application

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T046 [P] Add type hints to all functions across all modules
- [ ] T047 [P] Add Google-style docstrings to all functions and classes
- [ ] T048 Comprehensive error handling throughout application with rich formatting
- [ ] T049 Input validation improvements across all functions
- [ ] T050 Run quickstart validation to ensure application works as expected

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable
- **User Story 6 (P1)**: Can start after Foundational (Phase 2) - Integrates all other stories

### Within Each User Story

- Core implementation before integration
- Story complete before moving to next priority
- All user stories must be complete before Phase 9

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Different user stories can be worked on in parallel by different team members
- Models within a story marked [P] can run in parallel

---

## Parallel Example: User Story 1

```bash
# Launch all components for User Story 1 together:
Task: "Implement Task dataclass with id, title, description, completed attributes in src/models.py"
Task: "Create add_task method in operations module in src/operations.py"
Task: "Create input validation for add_task in src/ui.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Add User Story 6 → Test independently → Deploy/Demo
8. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
   - Developer F: User Story 6
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence