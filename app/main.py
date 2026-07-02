from fastapi import FastAPI
from app.schemas import Task
from fastapi import FastAPI, HTTPException

app = FastAPI()

tasks = []

@app.get("/")
def home():
    return {"message": "Todo API Running"}

@app.get("/tasks", response_model=list[Task])
def get_tasks():
    return tasks

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    tasks.append(task.dict())
    return task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: Task):
    if task_id >= len(tasks):
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    tasks[task_id] = task.dict()

    return tasks[task_id]


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    if task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")

    return tasks[task_id]

@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int):
    if task_id >= len(tasks):
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    deleted_task = tasks.pop(task_id)

    return deleted_task