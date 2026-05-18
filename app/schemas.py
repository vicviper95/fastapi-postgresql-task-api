# Pydantic request/response models
from pydantic import BaseModel
from typing import Optional

class TaskCreate(BaseModel):
  title: str

class TaskUpdate(BaseModel):
  title: Optional[str] = None
  completed: Optional[bool] = None

class Task(BaseModel):
  id: int
  title: str
  completed: bool = False

  class Config: 
    from_attributes = True  # This allows Pydantic to read data from SQLAlchemy models using attribute access, which is necessary for the response models to work correctly when returning SQLAlchemy model instances.
