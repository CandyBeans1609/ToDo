# Third-party libraries
from fastapi import HTTPException
from sqlalchemy.orm import Session

# Local imports
from app.models import Todo
from app.schemas import TaskCreate, TaskUpdate

def get_tasks(db: Session):
    return db.query(Todo).all()

def get_task(db:Session, task_id:int):
    todo = db.query(Todo).filter(Todo.id==task_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Task not found")
    return todo

def create_task(db:Session, task:TaskCreate):
    todo = Todo(title=task.title, completed=task.completed)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

def update_task(db:Session, task_id:int, task:TaskUpdate):
    todo = db.query(Todo).filter(Todo.id==task_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Task not found")
    todo.title = task.title
    todo.completed = task.completed
    db.commit()
    db.refresh(todo)
    return todo

def delete_task(db:Session, task_id:int):
    todo = db.query(Todo).filter(Todo.id==task_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(todo)
    db.commit()
    return {"message": "Task deleted successfully"}
