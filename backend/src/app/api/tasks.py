from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.api.deps import get_db
from app.models.task import Task, TaskCreate, TaskUpdate
from app.services.auth import get_current_user_id

router = APIRouter()

@router.get("/", response_model=List[Task])
def read_tasks(
    db: Session = Depends(get_db),
    current_user_id: str = Depends(get_current_user_id)
):
    tasks = db.exec(
        select(Task)
        .where(Task.user_id == current_user_id)
        .order_by(Task.position.asc(), Task.id.desc())
    ).all()
    return tasks

@router.post("/", response_model=Task)
def create_task(
    *,
    db: Session = Depends(get_db),
    task_in: TaskCreate,
    current_user_id: str = Depends(get_current_user_id)
):
    db_obj = Task.from_orm(task_in, update={"user_id": current_user_id})
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

@router.put("/{task_id}", response_model=Task)
def update_task(
    *,
    db: Session = Depends(get_db),
    task_id: int,
    task_in: TaskUpdate,
    current_user_id: str = Depends(get_current_user_id)
):
    db_obj = db.get(Task, task_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Task not found")
    if db_obj.user_id != current_user_id:
        raise HTTPException(status_code=403, detail="Not enough permissions")

    task_data = task_in.dict(exclude_unset=True)
    for key, value in task_data.items():
        setattr(db_obj, key, value)

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

@router.delete("/{task_id}", response_model=Task)
def delete_task(
    *,
    db: Session = Depends(get_db),
    task_id: int,
    current_user_id: str = Depends(get_current_user_id)
):
    db_obj = db.get(Task, task_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Task not found")
    if db_obj.user_id != current_user_id:
        raise HTTPException(status_code=403, detail="Not enough permissions")

    db.delete(db_obj)
    db.commit()
    return db_obj

@router.patch("/{task_id}/complete", response_model=Task)
def toggle_task_complete(
    *,
    db: Session = Depends(get_db),
    task_id: int,
    current_user_id: str = Depends(get_current_user_id)
):
    db_obj = db.get(Task, task_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Task not found")
    if db_obj.user_id != current_user_id:
        raise HTTPException(status_code=403, detail="Not enough permissions")

    db_obj.completed = not db_obj.completed
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
