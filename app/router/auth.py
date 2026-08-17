from fastapi import APIRouter, status, Depends
from app.schemas.user_schema import UserCreate, UserResponse, UserLogin
from sqlalchemy.orm import Session
from app.db.database import get_db
import app.services.user_service as user_service
from app.core.security import create_access_token, get_current_user

router = APIRouter(
    prefix="/api",
    tags=["Authentication"]
)

@router.post("/register", status_code=status.HTTP_201_CREATED, response_model= UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    data = user_service.create_user(db,user)
    return data

@router.post("/login", status_code=status.HTTP_200_OK)
def login_user(user: UserLogin, db:Session = Depends(get_db)):
    data = user_service.user_login(db,user)

    access_token = create_access_token(data={"sub":data.user_name, "id":data.id})

    return {
        "message": "Đăng nhập thành công",
        "access_token": access_token,
        "token_type": "bearer",
        "data": {
            "id": data.id,
            "email": data.email,
            "is_active": data.is_active,
            "created_at": data.created_at
        }
    }

@router.get("/profile")
def profile(username: str = Depends(get_current_user)):
    return {
        "message": f"Welcome, {username}!"
    }