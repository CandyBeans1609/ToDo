from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.services import user_service
from app.schemas import UserCreate, UserLogin, UserResponse

router = APIRouter()

@router.post("/users/register", response_model = UserResponse):
def create_user(user: UserCreate, db:Session = Depends(get_db)):
    return user_service.create_user(db, user)