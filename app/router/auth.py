from fastapi import APIRouter, status, Depends
from app.schemas.user_schema import UserCreate, UserResponse
from sqlalchemy.orm import Session
from app.db.database import get_db
import app.services.user_service as user_service

router = APIRouter(
    prefix="/api",
    tags=["Authentication"]
)

@router.post("/register", status_code=status.HTTP_201_CREATED, response_model= UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    data = user_service.create_user(db, user)
    return data
