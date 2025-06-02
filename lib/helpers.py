from models.event import Event
from models.guest import Guest
from models.venue import Venue
from models.event_guest import EventGuest
from sqlalchemy.orm.exc import NoResultFound
from datetime import datetime

# EVENTS
def create_event(session):
    try:
        name = input("Event name: ")
        description = input("Description: ")
        date_str = input("Date (YYYY-MM-DD): ")
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        venue_id = int(input("Venue ID: "))

        # Check for duplicate event by name and date
        existing = session.query(Event).filter_by(name=name, date=date).first()
        if existing:
            print(f"Event '{name}' on {date} already exists.")
            return None

        event = Event(name=name, description=description, date=date, venue_id=venue_id)
        session.add(event)
        print(f"Event '{name}' created!")
        return event
    except Exception as e:
        print(f"Failed to create event: {e}")
        return None

def list_events(session):
    try:
        events = session.query(Event).all()
        if not events:
            print("No events found.")
        for event in events:
            print(f"{event.id}: {event.name} on {event.date} @ Venue ID {event.venue_id}")
    except Exception as e:
        print(f"Failed to list events: {e}")

# GUESTS
def add_guest(session):
    try:
        name = input("Guest name: ")
        email = input("Email: ")
        phone = input("Phone number: ")

        # Check duplicate by email
        existing = session.query(Guest).filter_by(email=email).first()
        if existing:
            print(f"Guest with email '{email}' already exists.")
            return None

        guest = Guest(name=name, email=email, phone=phone)
        session.add(guest)
        print(f"Guest '{name}' added.")
        return guest
    except Exception as e:
        print(f"Failed to add guest: {e}")
        return None

def list_guests(session):
    try:
        guests = session.query(Guest).all()
        if not guests:
            print("No guests found.")
        for guest in guests:
            print(f"{guest.id}: {guest.name} | {guest.email} | {guest.phone}")
    except Exception as e:
        print(f"Failed to list guests: {e}")

# VENUES
def add_venue(session):
    try:
        name = input("Venue name: ")
        location = input("Location: ")
        capacity = input("Capacity: ")

        # Check duplicate by name and location
        existing = session.query(Venue).filter_by(name=name, location=location).first()
        if existing:
            print(f"Venue '{name}' at '{location}' already exists.")
            return None

        venue = Venue(name=name, location=location, capacity=int(capacity))
        session.add(venue)
        print(f"Venue '{name}' added.")
        return venue
    except Exception as e:
        print(f"Failed to add venue: {e}")
        return None

def list_venues(session):
    try:
        venues = session.query(Venue).all()
        if not venues:
            print("No venues found.")
        for venue in venues:
            print(f"{venue.id}: {venue.name} | {venue.location} | Capacity: {venue.capacity}")
    except Exception as e:
        print(f"Failed to list venues: {e}")

# RSVPs
def rsvp_guest_to_event(session):
    try:
        print("Guests:")
        list_guests(session)
        guest_id = int(input("Enter Guest ID: "))

        print("Events:")
        list_events(session)
        event_id = int(input("Enter Event ID: "))

        # Check if RSVP exists already
        existing = session.query(EventGuest).filter_by(guest_id=guest_id, event_id=event_id).first()
        if existing:
            print("This guest has already RSVP'd to this event.")
            return None

        rsvp = EventGuest(guest_id=guest_id, event_id=event_id)
        session.add(rsvp)
        print("RSVP recorded.")
        return rsvp
    except Exception as e:
        print(f"Failed to record RSVP: {e}")
        return None

def list_event_attendees(session):
    try:
        print("Events:")
        list_events(session)
        event_id = int(input("Enter Event ID: "))
        rsvps = session.query(EventGuest).filter_by(event_id=event_id).all()
        if not rsvps:
            print("No attendees found for this event.")
            return

        print(f"Attendees for event ID {event_id}:")
        for rsvp in rsvps:
            guest = session.query(Guest).get(rsvp.guest_id)
            if guest:
                print(f"{guest.name} | {guest.email}")
    except Exception as e:
        print(f"Failed to list attendees: {e}")

# Exit
def exit_program():
    print("Goodbye!")
    exit()
