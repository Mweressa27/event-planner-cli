from lib.models import Session, Event, Guest, RSVP
from datetime import date

session = Session()

class EventPlanner:
    def create_event(self, title, location, date):
        e = Event(title=title, location=location, date=date)
        session.add(e)
        session.commit()
        print(f"✅ Created event: {e}")

    def list_events(self):
        for e in session.query(Event).all():
            print(e)

    def add_guest(self, name, email):
        g = Guest(name=name, email=email)
        session.add(g)
        session.commit()
        print(f"✅ Guest added: {g}")

    def list_guests(self):
        for g in session.query(Guest).all():
            print(g)

    def rsvp(self, guest_id, event_id, status="yes"):
        r = RSVP(guest_id=guest_id, event_id=event_id, status=status)
        session.add(r)
        session.commit()
        print(f"✅ RSVP: {r}")

    def show_event_guests(self, event_id):
        event = session.get(Event, event_id)
        if event:
            for r in event.rsvps:
                print(f"{r.guest.name} - {r.status}")
        else:
            print("❌ Event not found.")

    def delete_event(self, event_id):
        event = session.get(Event, event_id)
        if event:
            session.delete(event)
            session.commit()
            print("🗑️ Event deleted.")
        else:
            print("❌ Not found.")
