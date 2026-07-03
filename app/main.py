from fastapi import FastAPI
from app.schemas import Task
from fastapi import FastAPI, HTTPException
from app.database import engine, Base, get_db
from app import models
from fastapi import Depends
from sqlalchemy.orm import Session
from app.models import Todo
 

Base.metadata.create_all(bind=engine)

app = FastAPI()

tasks = []

@app.get("/")
def home():
    return {"message": "Todo API Running"}

@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(models.Todo).all()

    return tasks

@app.post("/tasks")
def create_task(
    task: Task,
    db: Session = Depends(get_db)):
    todo = Todo(
        title=task.title,
        completed=task.completed
    )

    db.add(todo)
    db.commit()
    db.refresh(todo)

    return todo

@app.put("/tasks/{task_id}")
def update_task(
    task_id: int,
    task: Task,
    db: Session = Depends(get_db)
):
    todo = db.query(Todo).filter(Todo.id == task_id).first()

    if not todo:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    todo.title = task.title
    todo.completed = task.completed

    db.commit()
    db.refresh(todo)

    return todo


@app.get("/tasks/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(models.Todo.id == task_id).first()

    if not todo:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return todo

@app.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    todo = db.query(Todo).filter(Todo.id == task_id).first()

    if not todo:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    db.delete(todo)
    db.commit()

    return {
        "message": "Task deleted successfully"
    }