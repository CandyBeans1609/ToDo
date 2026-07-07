from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import TaskResponse, TaskCreate, TaskUpdate

from app.services import task_service

router = APIRouter()

@router.get("/")
def home():
    return {"message": "Todo API Running"}

@router.get("/tasks", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return task_service.get_tasks(db)

@router.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    return task_service.get_task(db, task_id)

@router.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate, db:Session = Depends(get_db)):
    return task_service.create_task(db, task)

@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskUpdate, db:Session = Depends(get_db)):
    return task_service.update_task(db, task_id, task)

@router.delete("/tasks/{task_id}", response_model=dict)
def delete_task(task_id: int, db:Session = Depends(get_db)):
    return task_service.delete_task(db, task_id)