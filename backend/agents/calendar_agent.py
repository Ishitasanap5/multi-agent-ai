from db.connection import SessionLocal
from db.models import Event

class CalendarAgent:

    def create_event(self, title: str, time: str):
        db = SessionLocal()

        event = Event(title=title, time=time)
        db.add(event)
        db.commit()
        db.refresh(event)

        return {
            "agent": "CalendarAgent",
            "action": "create_event",
            "data": {
                "id": event.id,
                "title": event.title,
                "time": event.time
            }
        }

    def get_all_events(self):
        db = SessionLocal()

        events = db.query(Event).all()

        return [
            {
                "id": event.id,
                "title": event.title,
                "time": event.time
            }
            for event in events
        ]