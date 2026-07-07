from fastapi import FastAPI

from app.database import Base, engine
from app.routers.tasks import router as task_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(task_router)