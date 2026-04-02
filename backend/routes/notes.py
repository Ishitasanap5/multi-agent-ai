from fastapi import APIRouter, Query
from agents.notes_agent import NotesAgent

router = APIRouter()
notes_agent = NotesAgent()


@router.post("/notes")
def create_note(title: str, content: str = ""):
    return notes_agent.create_note(title, content)


@router.get("/notes")
def get_notes():
    return notes_agent.get_all_notes()


@router.get("/notes/search")
def search_notes(keyword: str = Query(..., description="Keyword to search in notes")):
    return notes_agent.search_notes(keyword)