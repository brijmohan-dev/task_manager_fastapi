from pydantic import BaseModel
from datetime import datetime
from config import TaskStatus
from uuid import UUID

# Schema for create task
class CreateTask(BaseModel):
    title: str
    description: str | None
    status: TaskStatus = TaskStatus.PENDING

# Schema for update task
class UpdateTask(BaseModel):
    title: str | None
    status: TaskStatus | None

# Schema for task response
class TaskResponse(BaseModel):
    id: UUID
    title: str
    description: str | None
    status: TaskStatus
    created_at: datetime
    updated_at: datetime | None