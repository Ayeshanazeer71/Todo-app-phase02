# Phase II Todo Web App - Monorepo

## Project Structure

- `backend/`: FastAPI + SQLModel (Neon PostgreSQL)
- `frontend/`: Next.js 16+ + Better Auth + Tailwind
- `specs/`: Service and Feature specifications
  - `specs/overview.md`: Project summary
  - `specs/api/`: REST API documentation
  - `specs/database/`: Database schema
  - `specs/ui/`: UI components and page structure
  - `specs/features/`: Functional requirements

## Workflows

1. **Spec-Driven Development**: Always update/read specs in `specs/` before implementation.
2. **PHR Tracking**: Every prompt interaction is recorded in `history/prompts/`.
3. **ADR Usage**: Significant architectural decisions are documented in `history/adr/`.

## Reference Commands

- `/sp.spec`: Update specifications
- `/sp.plan`: Create implementation plans
- `/sp.tasks`: Generate tasks from plans
- `/sp.implement`: Execute tasks
