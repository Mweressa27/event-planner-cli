from models import Session
from models.event import Event
from models.guest import Guest
from models.venue import Venue
from models.event_guest import EventGuest
from datetime import datetime

def create_event(session):
    try:
        name = input("Event name: ")
        description = input("Description: ")
        date_str = input("Date (YYYY-MM-DD): ")
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        venue_id = int(input("Venue ID: "))
        event = Event(name=name, description=description, date=date, venue_id=venue_id)
        session.add(event)
        return event
    except Exception as e:
        print(f"Error: {e}")
        return None

def list_events(session):
    events = session.query(Event).all()
    for event in events:
        print(f"{event.id}: {event.name} on {event.date} @ Venue ID {event.venue_id}")

def update_event(session):
    list_events(session)
    try:
        event_id = int(input("Enter Event ID to update: "))
        event = session.query(Event).get(event_id)
        if not event:
            print("Event not found.")
            return
        event.name = input(f"New name [{event.name}]: ") or event.name
        event.description = input(f"New description [{event.description}]: ") or event.description
        new_date = input(f"New date (YYYY-MM-DD) [{event.date}]: ")
        if new_date:
            event.date = datetime.strptime(new_date, "%Y-%m-%d").date()
        print("Event updated.")
    except Exception as e:
        print(f"Error updating event: {e}")

def delete_event(session):
    list_events(session)
    try:
        event_id = int(input("Enter Event ID to delete: "))
        event = session.query(Event).get(event_id)
        if event:
            session.delete(event)
            print("Event deleted.")
        else:
            print("Event not found.")
    except Exception as e:
        print(f"Error: {e}")

def add_guest(session):
    try:
        name = input("Guest name: ")
        email = input("Email: ")
        phone = input("Phone number: ")
        guest = Guest(name=name, email=email, phone=phone)
        session.add(guest)
        return guest
    except Exception as e:
        print(f"Error: {e}")
        return None

def list_guests(session):
    guests = session.query(Guest).all()
    for guest in guests:
        print(f"{guest.id}: {guest.name} | {guest.email} | {guest.phone}")

def update_guest(session):
    list_guests(session)
    try:
        guest_id = int(input("Enter Guest ID to update: "))
        guest = session.query(Guest).get(guest_id)
        if guest:
            guest.name = input(f"New name [{guest.name}]: ") or guest.name
            guest.email = input(f"New email [{guest.email}]: ") or guest.email
            guest.phone = input(f"New phone [{guest.phone}]: ") or guest.phone
            print("Guest updated.")
        else:
            print("Guest not found.")
    except Exception as e:
        print(f"Error updating guest: {e}")

def delete_guest(session):
    list_guests(session)
    try:
        guest_id = int(input("Enter Guest ID to delete: "))
        guest = session.query(Guest).get(guest_id)
        if guest:
            session.delete(guest)
            print("Guest deleted.")
        else:
            print("Guest not found.")
    except Exception as e:
        print(f"Error: {e}")

def add_venue(session):
    try:
        name = input("Venue name: ")
        location = input("Location: ")
        capacity = int(input("Capacity: "))
        venue = Venue(name=name, location=location, capacity=capacity)
        session.add(venue)
        return venue
    except Exception as e:
        print(f"Error: {e}")
        return None

def list_venues(session):
    venues = session.query(Venue).all()
    for venue in venues:
        print(f"{venue.id}: {venue.name} | {venue.location} | Capacity: {venue.capacity}")

def rsvp_guest_to_event(session):
    try:
        list_guests(session)
        guest_id = int(input("Enter Guest ID: "))
        list_events(session)
        event_id = int(input("Enter Event ID: "))
        existing = session.query(EventGuest).filter_by(guest_id=guest_id, event_id=event_id).first()
        if existing:
            print("Guest already RSVP'd to this event.")
            return None
        rsvp = EventGuest(guest_id=guest_id, event_id=event_id)
        session.add(rsvp)
        return rsvp
    except Exception as e:
        print(f"Error: {e}")
        return None

def list_event_attendees(session):
    list_events(session)
    try:
        event_id = int(input("Enter Event ID: "))
        rsvps = session.query(EventGuest).filter_by(event_id=event_id).all()
        for rsvp in rsvps:
            guest = session.query(Guest).get(rsvp.guest_id)
            print(f"{guest.name} | {guest.email}")
    except Exception as e:
        print(f"Error: {e}")

def exit_program():
    print("Goodbye!")
    exit()
