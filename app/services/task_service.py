from typing import Optional

from sqlalchemy.orm import Session

from app.models import TaskModel
from app.schemas import TaskCreate, TaskUpdate

def get_tasks(db: Session, completed: Optional[bool] = None):
  query = db.query(TaskModel)

  if completed is not None:
    query = query.filter(TaskModel.completed == completed)

  return query.all()

def create_task(db: Session, task_data: TaskCreate):
  new_task = TaskModel(
    title = task_data.title, 
    completed=False 
  )

  db.add(new_task)
  db.commit()
  db.refresh(new_task)

  return new_task

def get_task(db: Session, task_id: int):
  return db.query(TaskModel).filter(TaskModel.id == task_id).first()

def update_task(db: Session, task_id: int, task_data: TaskUpdate):
  task = get_task(db, task_id)

  if not task:
    return None
  
  if task_data.title is not None:
    task.title = task_data.title

  if task_data.completed is not None:
    task.completed = task_data.completed

  db.commit()
  db.refresh(task)

  return task

def toggle_task(db: Session, task_id: int):
  task = get_task(db, task_id)

  if not task:
    return None
  
  task.completed = not task.completed

  db.commit()
  db.refresh(task)

  return task

def delete_task(db: Session, task_id: int):
  task = get_task(db, task_id)

  if not task:
    return False
  
  db.delete(task)
  db.commit()

  return True