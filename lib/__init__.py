# lib/setup_db.py

from models import Base, engine
from models.event import Event
from models.guest import Guest
from models.venue import Venue
from models.event_guest import EventGuest

def create_tables():
    Base.metadata.create_all(engine)
    print("All tables created successfully.")

if __name__ == "__main__":
    create_tables()
