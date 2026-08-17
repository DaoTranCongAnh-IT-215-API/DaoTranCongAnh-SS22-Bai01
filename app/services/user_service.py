from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate, UserLogin
from app.models.user_model import User
from fastapi import HTTPException, status
from app.core.security import hash_password

def create_user(db: Session, user: UserCreate):
    exit_user = db.query(User).filter(User.user_name == user.user_name).first()

    if exit_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username đã tồn tại")

    hasded_password = hash_password(user.password)
    new_user = User(
        user_name = user.user_name,
        hashed_password = user.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def user_login(db: Session, user: UserLogin):
    exit_user = db.query(User).filter(User.user_name == user.user_name).first()

    if not exit_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")

    exit_password = db.query(User).filter(User.hashed_password == user.password).first()
    hashed_password = hash_password(user.password)

    if not exit_password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")

    return user