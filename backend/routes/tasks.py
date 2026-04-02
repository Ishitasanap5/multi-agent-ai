from fastapi import APIRouter
from db.connection import SessionLocal
from db.models import Task

router = APIRouter()

@router.post("/tasks")
def create_task(title: str):
    db = SessionLocal()

    task = Task(title=title, status="pending")
    db.add(task)
    db.commit()
    db.refresh(task)

    return {
        "id": task.id,
        "title": task.title,
        "status": task.status
    }