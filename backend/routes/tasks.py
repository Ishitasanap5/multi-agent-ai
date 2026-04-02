from fastapi import APIRouter
from agents.task_agent import TaskAgent

router = APIRouter()

# Initialize agent
task_agent = TaskAgent()


# ✅ Create Task (uses agent)
@router.post("/tasks")
def create_task(title: str):
    return task_agent.create_task(title)


# ✅ Get All Tasks (optional but VERY useful)
@router.get("/tasks")
def get_tasks():
    return task_agent.get_all_tasks()