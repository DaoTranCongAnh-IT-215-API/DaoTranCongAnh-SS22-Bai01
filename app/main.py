from fastapi import FastAPI
from app.db.database import Base,engine
from app.models.user_model import User
app = FastAPI(
    title="Manager DevConnect"
)

Base.metadata.create_all(bind=engine)
@app.get("/")
def get_root():
    return {"message: server đang chạy"}