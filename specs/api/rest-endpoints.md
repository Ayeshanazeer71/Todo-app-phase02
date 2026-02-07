# API Specification: REST Endpoints

All API endpoints reside under `/api/`. JWT authentication is mandatory for all task-related endpoints.

## Authentication
Better Auth handles the issuance of JWTs. The backend validates the `Authorization: Bearer <token>` header.

## Endpoints

### Tasks
- **GET /api/tasks**: Fetch all tasks for the authenticated user.
- **POST /api/tasks**: Create a new task.
- **GET /api/tasks/{id}**: Fetch a single task by ID (must belong to user).
- **PUT /api/tasks/{id}**: Update task title/description.
- **DELETE /api/tasks/{id}**: Delete a task.
- **PATCH /api/tasks/{id}/complete**: Toggle completion status.

## Schemas

### TaskBase (input)
- `title`: String (required)
- `description`: String (optional)

### Task (output)
- `id`: Integer
- `title`: String
- `description`: String
- `completed`: Boolean
- `user_id`: String (owner)

## Error Handling
- `401 Unauthorized`: Missing or invalid JWT.
- `403 Forbidden`: Accessing a task not owned by the user.
- `404 Not Found`: Resource does not exist.
- `422 Unprocessable Entity`: Validation error.
