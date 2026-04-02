from fastapi import APIRouter
from agents.calendar_agent import CalendarAgent

router = APIRouter()
calendar_agent = CalendarAgent()

@router.post("/events")
def create_event(title: str, time: str):
    return calendar_agent.create_event(title, time)

@router.get("/events")
def get_events():
    return calendar_agent.get_all_events()