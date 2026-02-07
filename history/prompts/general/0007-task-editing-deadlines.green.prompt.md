---
id: 7
title: Task Editing and Deadlines
stage: green
date: 2026-01-06
surface: agent
model: claude-sonnet-4-5-20250929
feature: task-edit-deadline
branch: main
user: default
command: none
labels: [dynamic-ui, dates, crud]
links:
  spec: specs/features/task-crud.md
  ticket: null
  adr: null
  pr: null
files:
  - backend/src/app/models/task.py
  - frontend/src/app/page.tsx
tests:
  - none
---

## Prompt

Add task editing and deadline dates

## Response snapshot

Implemented backend support for deadline dates (ISO-8601). Updated the frontend with an inline editing state, a native date picker, and visual indicators for overdue tasks. Users can now modify all task fields and track completion by date.

## Outcome

- ✅ Impact: Complete CRUD lifecycle and basic time management.
- 🧪 Tests: n/a
- 📁 Files: backend/src/app/models/task.py, frontend/src/app/page.tsx
- 🧠 Reflection: Overdue tasks are highlighted with a red badge for immediate visual feedback.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): n/a
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): none
