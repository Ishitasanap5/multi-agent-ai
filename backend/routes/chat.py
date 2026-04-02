from fastapi import APIRouter
from agents.orchestrator import Orchestrator

router = APIRouter()
orchestrator = Orchestrator()

@router.post("/chat")
def chat(user_input: str):
    return orchestrator.handle_request(user_input)