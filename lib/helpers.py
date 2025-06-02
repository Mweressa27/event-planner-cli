from models import session
from models.event import Event
from models.guest import Guest
from models.venue import Venue
from models.event_guest import EventGuest
from datetime import datetime

# EVENTS
def create_event():
    name = input("Event name: ")
    description = input("Description: ")
    date_str = input("Date (YYYY-MM-DD): ")
    date = datetime.strptime(date_str, "%Y-%m-%d").date()
    venue_id = int(input("Venue ID: "))
    event = Event(name=name, description=description, date=date, venue_id=venue_id)
    session.add(event)
    session.commit()
    print(f"Event '{name}' created!")

def list_events():
    events = session.query(Event).all()
    for event in events:
        print(f"{event.id}: {event.name} on {event.date} @ Venue ID {event.venue_id}")

# GUESTS
def add_guest():
    name = input("Guest name: ")
    email = input("Email: ")
    phone = input("Phone number: ")
    guest = Guest(name=name, email=email, phone=phone)
    session.add(guest)
    session.commit()
    print(f"Guest '{name}' added.")

def list_guests():
    guests = session.query(Guest).all()
    for guest in guests:
        print(f"{guest.id}: {guest.name} | {guest.email} | {guest.phone}")

# VENUES
def add_venue():
    name = input("Venue name: ")
    location = input("Location: ")
    capacity = input("Capacity: ")
    venue = Venue(name=name, location=location, capacity=int(capacity))
    session.add(venue)
    session.commit()
    print(f"Venue '{name}' added.")

def list_venues():
    venues = session.query(Venue).all()
    for venue in venues:
        print(f"{venue.id}: {venue.name} | {venue.location} | Capacity: {venue.capacity}")

# RSVPs
def rsvp_guest_to_event():
    list_guests()
    guest_id = int(input("Enter Guest ID: "))
    list_events()
    event_id = int(input("Enter Event ID: "))
    rsvp = EventGuest(guest_id=guest_id, event_id=event_id)
    session.add(rsvp)
    session.commit()
    print("RSVP recorded.")

def list_event_attendees():
    list_events()
    event_id = int(input("Enter Event ID: "))
    rsvps = session.query(EventGuest).filter_by(event_id=event_id).all()
    for rsvp in rsvps:
        guest = session.query(Guest).get(rsvp.guest_id)
        print(f"{guest.name} | {guest.email}")

# Exit
def exit_program():
    print("Goodbye!")
    exit()
