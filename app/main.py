from fastapi import FastAPI
from app.db.database import Base,engine
import app.models.user_model 
from app.router.auth import router

app = FastAPI(
    title="Manager DevConnect"
)

Base.metadata.create_all(bind=engine)
app.include_router(router)

@app.get("/")
def get_root():
    return {"message: server đang chạy"}