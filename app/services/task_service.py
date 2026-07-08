# Third-party libraries
from fastapi import HTTPException
from sqlalchemy.orm import Session

# Local imports
from app.models import Todo
from app.schemas import TaskCreate, TaskUpdate
from app.models import User

def get_tasks(db: Session, current_user: User):
    return db.query(Todo).filter(Todo.user_id == current_user.id).all()

def get_task(db:Session, task_id:int, current_user: User):
    todo = db.query(Todo).filter(Todo.id==task_id, Todo.user_id == current_user.id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Task not found")
    return todo

def create_task(db:Session, task:TaskCreate, current_user: User):
    todo = Todo(title=task.title, completed=task.completed, user_id=current_user.id)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

def update_task(db:Session, task_id:int, task:TaskUpdate, current_user: User):
    todo = db.query(Todo).filter(Todo.id==task_id, Todo.user_id == current_user.id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Task not found")
    todo.title = task.title
    todo.completed = task.completed
    db.commit()
    db.refresh(todo)
    return todo

def delete_task(db:Session, task_id:int, current_user: User):
    todo = db.query(Todo).filter(Todo.id==task_id, Todo.user_id == current_user.id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(todo)
    db.commit()
    return {"message": "Task deleted successfully"}
