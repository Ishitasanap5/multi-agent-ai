from db.connection import SessionLocal
from db.models import Task

class TaskAgent:

    def create_task(self, title: str):
        db = SessionLocal()

        task = Task(title=title, status="pending")
        db.add(task)
        db.commit()
        db.refresh(task)

        return {
            "agent": "TaskAgent",
            "action": "create_task",
            "data": {
                "id": task.id,
                "title": task.title,
                "status": task.status
            }
        }

    def get_all_tasks(self):
        db = SessionLocal()

        tasks = db.query(Task).all()

        return [
            {
                "id": task.id,
                "title": task.title,
                "status": task.status
            }
            for task in tasks
        ]