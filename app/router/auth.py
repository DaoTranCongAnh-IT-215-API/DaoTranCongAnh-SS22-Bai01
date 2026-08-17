from fastapi import APIRouter, status, Depends
from app.schemas.user_schema import UserCreate, UserResponse, UserLogin
from sqlalchemy.orm import Session
from app.db.database import get_db
import app.services.user_service as user_service, user_login

router = APIRouter(
    prefix="/api",
    tags=["Authentication"]
)

@router.post("/register", status_code=status.HTTP_201_CREATED, response_model= UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    data = user_service.create_user(db,user)
    return data

@router.post("/login", status_code=status.HTTP_200_OK, response_model=UserResponse)
def login_user(user: UserLogin, db:Session = Depends(get_db)):
    data = user