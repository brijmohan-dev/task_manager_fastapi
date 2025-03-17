from fastapi import APIRouter, HTTPException
from schemas import CreateTask, TaskResponse, UpdateTask
from typing import List
from uuid import UUID
import models
from database import db_dependency
import logging

# Router
router = APIRouter(
    prefix='/tasks',
    tags=['task']
)

# Constansts
INTERNAL_SERVER_ERROR = "Internal Server Error"
TASK_NOT_FOUND = "Task not found"

# Add task route
@router.post("/", response_model=TaskResponse)
async def create_task(task: CreateTask, db: db_dependency):
    try:
        new_task = models.Task(**task.model_dump())
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        return new_task
    except Exception as e:
        logging.error('Error while adding a task', e)
        raise HTTPException(status_code = 500, detail = INTERNAL_SERVER_ERROR)

# Get all tasks route
@router.get("/", response_model=List[TaskResponse])
async def get_tasks(db: db_dependency, skip: int = 0, limit: int = 10):
    try:
        tasks = db.query(models.Task).offset(skip).limit(limit).all()
        return tasks
    except Exception as e:
        logging.error('Error while fetching all tasks', e)
        raise HTTPException(status_code = 500, detail = INTERNAL_SERVER_ERROR)

# Update a task route
@router.put("/{task_id}", response_model=TaskResponse)
async def update_task(task_id: UUID, task_update: UpdateTask, db: db_dependency):
    try:
        task = db.query(models.Task).filter(models.Task.id == task_id).first()
        if not task:
            logging.error(f'Task with id {task_id} not found')
            raise HTTPException(status_code = 404, detail=TASK_NOT_FOUND)
        for key, value in task_update.model_dump(exclude_unset=True).items():
            setattr(task, key, value)
        db.commit()
        db.refresh(task)
        return task
    except Exception as e:
        logging.error('Error while updating a task', e)
        raise HTTPException(status_code = 500, detail = INTERNAL_SERVER_ERROR)

# Delete a task route
@router.delete("/{task_id}")
async def delete_task(task_id: UUID, db: db_dependency):
    try:
        task = db.query(models.Task).filter(models.Task.id == task_id).first()
        if not task:
            logging.error(f'Task with id {task_id} not found')
            raise HTTPException(status_code = 404, detail = TASK_NOT_FOUND)
        db.delete(task)
        db.commit()
        return {"message": "Task deleted successfully"}
    except Exception as e:
        logging.error('Error while deleting a task', e)
        raise HTTPException(status_code = 500, detail = INTERNAL_SERVER_ERROR)

