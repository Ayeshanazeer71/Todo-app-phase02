---
id: 1
title: Create Todo Constitution
stage: constitution
date: 2025-12-31
surface: agent
model: Claude Sonnet 4.5
feature: todo-app
branch: master
user: user
command: /sp.constitution
labels: [constitution, todo-app, python]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

Create the project constitution for a simple in-memory Python console Todo app.

Key principles:
- Use Python 3.13+ with type hints and clean code.
- In-memory storage only (list of tasks).
- Task model: id (auto-increment int), title (str), description (str), completed (bool, default False).
- Menu-driven console interface with clear prompts.
- Proper error handling (e.g., invalid ID, no tasks).
- No external dependencies (pure stdlib).
- Project structure: /src with main.py and any modules.
- Follow spec-driven development: no manual coding, only refine specs.
- Focus on basic 5 features: Add, List/View, Update, Delete, Mark Complete.

## Response snapshot

Created the Todo Console App Constitution with 6 core principles:
1. Python 3.13+ with Type Hints
2. In-Memory Storage Only
3. Clean Task Model
4. Menu-Driven Console Interface
5. Comprehensive Error Handling
6. Pure Standard Library Dependencies

Plus additional sections for Project Structure, Development Workflow, and Governance. The constitution establishes the required task model and development constraints.

## Outcome

- ✅ Impact: Created initial project constitution at .specify/memory/constitution.md
- 🧪 Tests: none
- 📁 Files: 1 file updated (.specify/memory/constitution.md)
- 🔁 Next prompts: Develop spec for the todo app based on constitution
- 🧠 Reflection: Constitution clearly defines the scope and constraints for the todo app development

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Create the feature spec based on this constitution