from fastapi import FastAPI
from db.connection import engine
from db.models import Base
from routes.tasks import router as task_router
app = FastAPI()
app.include_router(task_router)
# Create tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Backend is running 🚀"}