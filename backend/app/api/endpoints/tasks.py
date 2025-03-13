from fastapi import APIRouter, HTTPException
from typing import List
from app.models.task import Task
from app.schemas.task import Task as TaskSchema
from app.db.session import get_db_session

router = APIRouter()

@router.post("/", response_model=TaskSchema)
async def create_task(task: TaskSchema):
    db = get_db_session()
    new_task = Task(**task.dict())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.get("/", response_model=List[TaskSchema])
async def get_tasks():
    db = get_db_session()
    tasks = db.query(Task).all()
    return tasks

@router.get("/{task_id}", response_model=TaskSchema)
async def get_task(task_id: int):
    db = get_db_session()
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=TaskSchema)
async def update_task(task_id: int, task: TaskSchema):
    db = get_db_session()
    existing_task = db.query(Task).filter(Task.id == task_id).first()
    if existing_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    for key, value in task.dict().items():
        setattr(existing_task, key, value)
    
    db.commit()
    db.refresh(existing_task)
    return existing_task

@router.delete("/{task_id}", response_model=dict)
async def delete_task(task_id: int):
    db = get_db_session()
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    db.delete(task)
    db.commit()
    return {"status": "success", "message": "Task deleted successfully"}