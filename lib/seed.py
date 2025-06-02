from lib.models import Base, engine, Session
from lib.models.event import Event
from lib.models.guest import Guest
from lib.models.venue import Venue
from lib.models.event_guest import EventGuest
from faker import Faker
import random

def seed_database():    
    fake = Faker()
    session = Session()
   
    Base.metadata.create_all(engine)

    # Seed Venues 
    venues = [
        Venue(
            name=fake.company(),
            location=fake.city(),
            capacity=random.randint(50, 200)
        ) for _ in range(3)
    ]
    session.add_all(venues)
    session.commit()
    print(f"✅ Seeded {len(venues)} venues.")

    # Seed Events 
    events = []
    for _ in range(5):
        event = Event(
            name=fake.catch_phrase(),
            description=fake.text(max_nb_chars=50),
            date=fake.date_between(start_date='today', end_date='+30d'),
            venue_id=random.choice(venues).id
        )
        events.append(event)
    session.add_all(events)
    session.commit()
    print(f"✅ Seeded {len(events)} events.")

    # Seed Guests 
    guests = [
        Guest(
            name=fake.name(),
            email=fake.email(),
            phone=fake.phone_number()
        ) for _ in range(10)
    ]
    session.add_all(guests)
    session.commit()
    print(f"✅ Seeded {len(guests)} guests.")

    # Seed RSVPs 
    rsvps = []
    for guest in guests:
        # Each guest RSVPs to 1 or 2 random events
        events_to_rsvp = random.sample(events, k=random.randint(1, 2))
        for event in events_to_rsvp:
            rsvp = EventGuest(guest_id=guest.id, event_id=event.id)
            rsvps.append(rsvp)
    session.add_all(rsvps)
    session.commit()
    print(f"✅ Seeded {len(rsvps)} RSVPs.")

    session.close()
    print("\n🎉 Database seeding complete. Ready to use your CLI!")

if __name__ == "__main__":
    seed_database()
