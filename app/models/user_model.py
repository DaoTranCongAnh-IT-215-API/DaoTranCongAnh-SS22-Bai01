from sqlalchemy import Column, String, Integer, Float, ForeignKey
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key= True, autoincrement= True, index= True)
    user_name = Column(String(100), nullable= False, unique= True)
    hashed_password = Column(String(100), nullable= False)
    