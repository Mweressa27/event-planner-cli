from lib.models import Session, Base, engine, Event, Guest, RSVP
from datetime import date
from faker import Faker
import random

session = Session()
fake = Faker()

# Seed Events
events = [Event(title=fake.catch_phrase(), location=fake.city(), date=fake.date_this_year()) for _ in range(5)]
session.add_all(events)
session.commit()

# Seed Guests
guests = [Guest(name=fake.name(), email=fake.email()) for _ in range(10)]
session.add_all(guests)
session.commit()

# Seed RSVPs
for guest in guests:
    rsvp = RSVP(
        guest_id=guest.id,
        event_id=random.choice(events).id,
        status=random.choice(["yes", "no", "maybe"])
    )
    session.add(rsvp)

session.commit()
