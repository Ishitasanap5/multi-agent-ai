from fastapi import FastAPI
from db.connection import engine
from db.models import Base
from routes.tasks import router as task_router
from agents.task_agent import TaskAgent
from routes.events import router as event_router
from routes.chat import router as chat_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Backend is running 🚀"}

# test agent
task_agent = TaskAgent()

@app.get("/test-agent")
def test_agent():
    return task_agent.create_task("Learn Agents")

# include routes
app.include_router(task_router)
app.include_router(event_router)
app.include_router(chat_router)