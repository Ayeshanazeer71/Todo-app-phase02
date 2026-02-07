# Feature: Authentication

## Overview
Phase II uses Better Auth for frontend/backend authentication. The backend validates JWTs issued by the frontend/Better Auth stack.

## JWT Issuance
- Handled via `Better Auth` on the Next.js side.
- SECRET MUST be shared via `BETTER_AUTH_SECRET` / `JWT_SECRET`.

## Constraints
- Login required for all `/api/tasks` access.
- Strict token validation on every backend request.
- Password hashing on backend uses bcrypt if manual users are handled.
