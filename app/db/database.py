from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "mysql+pymysql://root:123456@localhost:3306/manager_db"

engine = create_engine(DATABASE_URL)

class Base(DeclarativeBase):
    pass

LocalSession = sessionmaker(autocommit = False, autoflush= False, bind= engine)

def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()