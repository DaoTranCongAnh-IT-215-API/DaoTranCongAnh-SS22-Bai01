from pydantic import BaseModel

class UserBase(BaseModel):
    user_name: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int

class UserLogin(UserBase):
    password: str