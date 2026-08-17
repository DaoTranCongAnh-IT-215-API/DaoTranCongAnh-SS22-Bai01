from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate
from app.models.user_model import User
from fastapi import HTTPException, status
from app.core.security import hash_password

def create_user(db: Session, user: UserCreate):
    exit_user = db.query(User).filter(User.user_name == user.username).first()

    if exit_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username đã tồn tại")

    hasded_password = hash_password(user.password)
    new_user = User(
        user_name = user.username,
        hashed_password = user.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
