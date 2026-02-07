# Database Schema: Phase II

Using Neon PostgreSQL with SQLModel.

## Tables

### Users (managed by Better Auth)
Extends or interfaces with the default Better Auth schema.

### Tasks
- `id`: Integer (Primary Key, Auto-increment)
- `title`: String (VARCHAR, NOT NULL)
- `description`: String (TEXT, NULLABLE)
- `completed`: Boolean (Default: FALSE)
- `user_id`: String (Foreign Key to User, Indexed)

## Isolation Rules
- Every query MUST filter by `user_id`.
- Indexes: `idx_tasks_user_id` for efficient filtering.
