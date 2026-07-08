from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import TaskResponse, TaskCreate, TaskUpdate

from app.services import task_service
from app.models import User
from app.security import get_current_user

router = APIRouter()

@router.get("/")
def home():
    return {"message": "Todo API Running"}

@router.get("/tasks", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return task_service.get_tasks(db, current_user)

@router.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return task_service.get_task(db, task_id, current_user)

@router.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return task_service.create_task( db, task, current_user)

@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskUpdate, db:Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return task_service.update_task(db, task_id, task, current_user)

@router.delete("/tasks/{task_id}", response_model=dict)
def delete_task(task_id: int, db:Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return task_service.delete_task(db, task_id, current_user)