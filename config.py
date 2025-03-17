import os
from enum import Enum

# Get the database URL from environment variable
DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://postgres:Brij%401234@localhost:5432/task_manager" )

# Enum for Task Status
class TaskStatus(str,Enum):
    PENDING = "pending"
    IN_PROGRESS = "in-progress"
    COMPLETED = "completed"