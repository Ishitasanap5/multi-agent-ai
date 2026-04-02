from db.connection import SessionLocal
from db.models import Note


class NotesAgent:
  

    def create_note(self, title: str, content: str = "") -> dict:
        db = SessionLocal()
        try:
            note = Note(title=title, content=content)
            db.add(note)
            db.commit()
            db.refresh(note)
            return {
                "agent": "NotesAgent",
                "action": "create_note",
                "data": {
                    "id": note.id,
                    "title": note.title,
                    "content": note.content
                }
            }
        finally:
            db.close()

    def get_all_notes(self) -> list[dict]:
        db = SessionLocal()
        try:
            notes = db.query(Note).all()
            return [
                {"id": n.id, "title": n.title, "content": n.content}
                for n in notes
            ]
        finally:
            db.close()

    def search_notes(self, keyword: str) -> list[dict]:
        """Search notes by keyword in title or content."""
        db = SessionLocal()
        try:
            results = db.query(Note).filter(
                Note.title.contains(keyword) | Note.content.contains(keyword)
            ).all()
            return [
                {"id": n.id, "title": n.title, "content": n.content}
                for n in results
            ]
        finally:
            db.close()