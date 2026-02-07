from typing import Optional, List, Dict
from sqlmodel import Field, SQLModel, JSON, Column
from datetime import date
from enum import Enum

class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class Subtask(SQLModel):
    title: str
    completed: bool = False

class TaskBase(SQLModel):
    title: str = Field(index=True)
    description: Optional[str] = None
    completed: bool = Field(default=False)
    deadline: Optional[date] = None
    priority: Priority = Field(default=Priority.MEDIUM)
    category: Optional[str] = Field(default="General", index=True)
    subtasks: List[Dict] = Field(default=[], sa_column=Column(JSON))
    position: Optional[int] = Field(default=0)

class Task(TaskBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: str = Field(index=True)

class TaskCreate(TaskBase):
    pass

class TaskUpdate(SQLModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    deadline: Optional[date] = None
    priority: Optional[Priority] = None
    category: Optional[str] = None
    subtasks: Optional[List[Dict]] = None
    position: Optional[int] = None
