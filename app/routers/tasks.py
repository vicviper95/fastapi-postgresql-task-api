from typing import List, Optional

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import Task, TaskCreate, TaskUpdate
from app.services import task_service

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("", response_model=List[Task])
def get_tasks(
  completed: Optional[bool] = None,
  db: Session = Depends(get_db)
):
  return task_service.get_tasks(db, completed)

@router.post("", response_model=Task)
def create_task(task_data: TaskCreate, db: Session = Depends(get_db)):
  return task_service.create_task(db, task_data)

@router.get("/{task_id}", response_model=Task)
def get_task(task_id: int, db: Session = Depends(get_db)):
  task = task_service.get_task(db, task_id)

  if not task:
    raise HTTPException(status_code=404, detail="Task not found")
  
  return task

@router.put("/{task_id}", response_model=Task)
def update_task(
  task_id: int,
  task_data: TaskUpdate,
  db: Session = Depends(get_db)
):
  task = task_service.update_task(db, task_id, task_data)

  if not task:
    raise HTTPException(status_code=404, detail="Task not found")
  
  return task

@router.patch("/{task_id}/toggle", response_model=Task)
def toggle_task(task_id: int, db: Session = Depends(get_db)):
  task = task_service.toggle(db, task_id)
  
  if not task:
    raise HTTPException(status_code=404, detauk="Task not found")
  
  return task

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
  deleted = task_service.delete_task(db, task_id)
  
  if not deleted:
    raise HTTPException(status_code=404, detail="Task not found")
  
  return {"message": "Task deleted"}