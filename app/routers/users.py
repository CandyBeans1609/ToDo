from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User
from app.schemas import UserCreate, UserLogin, UserResponse, Token
from app.security import get_current_user
from app.services import user_service

router = APIRouter()


@router.post("/users/register", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)


@router.post("/users/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    return user_service.login_user(db, user)


@router.get("/users/me", response_model=UserResponse)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
