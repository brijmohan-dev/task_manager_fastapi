# Application to manage a "Task Management System" with the following features:

## API Endpoints:
1. Create a Task: Accept title, description, and status fields (status can be pending, in-progress, or completed).
2. Get All Tasks: Return a list of tasks with pagination (default: 10 tasks per page).
3. Update a Task: Allow updating the title and status of a task by its ID.
4. Delete a Task: Remove a task by its ID.

## Database:
Use PostgreSQL to store tasks.
Create a table tasks with columns:
id (Primary Key, UUID)
title (String, Required)
description (String, Optional)
status (Enum: pending, in-progress, completed)
created_at (Timestamp, Default: Current Time)
updated_at (Timestamp, Auto-Update on Modify)
Requirements:

Write a FastAPI application that includes the above endpoints.

Use SQLAlchemy or any ORM for database interactions.

Write the database schema and migration script for PostgreSQL using Alembic.

Add proper exception handling and validation using Pydantic models.

Implement a health-check endpoint for database connectivity.

