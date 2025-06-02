from helpers import (
    create_event, list_events,
    add_guest, list_guests,
    add_venue, list_venues,
    rsvp_guest_to_event, list_event_attendees,
    exit_program
)
from models import Session  

def menu():
    print("\n=== Event Planner CLI ===")
    print("1. Create Event")
    print("2. List Events")
    print("3. Add Guest")
    print("4. List Guests")
    print("5. Add Venue")
    print("6. List Venues")
    print("7. RSVP Guest to Event")
    print("8. View Event Attendees")
    print("0. Exit")

def main():
    session = Session()  
    try:
        while True:
            menu()
            choice = input("> ")
            if choice == "1":
                result = create_event(session)
                if result:
                    session.commit()
                else:
                    session.rollback()
            elif choice == "2":
                list_events(session)
            elif choice == "3":
                result = add_guest(session)
                if result:
                    session.commit()
                else:
                    session.rollback()
            elif choice == "4":
                list_guests(session)
            elif choice == "5":
                result = add_venue(session)
                if result:
                    session.commit()
                else:
                    session.rollback()
            elif choice == "6":
                list_venues(session)
            elif choice == "7":
                result = rsvp_guest_to_event(session)
                if result:
                    session.commit()
                else:
                    session.rollback()
            elif choice == "8":
                list_event_attendees(session)
            elif choice == "0":
                session.close()
                exit_program()
            else:
                print("Invalid input.")
    except KeyboardInterrupt:
        print("\nExiting program.")
        session.close()

if __name__ == "__main__":
    main()
