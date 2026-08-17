from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    user_name: str

class UserCreate(UserBase):
    password: str

class UserLogin(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    class Config:
        from_attributes = True

