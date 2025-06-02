from helpers import (
    create_event, list_events, update_event, delete_event,
    add_guest, list_guests, update_guest, delete_guest,
    add_venue, list_venues,
    rsvp_guest_to_event, list_event_attendees,
    exit_program
)
from models import Session

def menu():
    print("\n=== 📅 Event Planner CLI ===")
    print("1. Create Event")
    print("2. List Events")
    print("3. Add Guest")
    print("4. List Guests")
    print("5. Add Venue")
    print("6. List Venues")
    print("7. RSVP Guest to Event")
    print("8. View Event Attendees")
    print("9. Update Event")
    print("10. Update Guest")
    print("11. Delete Event")
    print("12. Delete Guest")
    print("0. Exit")

def main():
    session = Session()
    try:
        while True:
            menu()
            choice = input("> ")
            if choice == "1":
                if create_event(session): session.commit()
            elif choice == "2":
                list_events(session)
            elif choice == "3":
                if add_guest(session): session.commit()
            elif choice == "4":
                list_guests(session)
            elif choice == "5":
                if add_venue(session): session.commit()
            elif choice == "6":
                list_venues(session)
            elif choice == "7":
                if rsvp_guest_to_event(session): session.commit()
            elif choice == "8":
                list_event_attendees(session)
            elif choice == "9":
                update_event(session)
                session.commit()
            elif choice == "10":
                update_guest(session)
                session.commit()
            elif choice == "11":
                delete_event(session)
                session.commit()
            elif choice == "12":
                delete_guest(session)
                session.commit()
            elif choice == "0":
                session.close()
                exit_program()
            else:
                print("❌ Invalid input.")
    except KeyboardInterrupt:
        session.close()
        print("\n👋 Exiting gracefully...")

if __name__ == "__main__":
    main()
