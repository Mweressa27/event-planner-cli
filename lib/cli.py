from helpers import (
    create_event, list_events,
    add_guest, list_guests,
    add_venue, list_venues,
    rsvp_guest_to_event, list_event_attendees,
    exit_program
)

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
    while True:
        menu()
        choice = input("> ")
        if choice == "1":
            create_event()
        elif choice == "2":
            list_events()
        elif choice == "3":
            add_guest()
        elif choice == "4":
            list_guests()
        elif choice == "5":
            add_venue()
        elif choice == "6":
            list_venues()
        elif choice == "7":
            rsvp_guest_to_event()
        elif choice == "8":
            list_event_attendees()
        elif choice == "0":
            exit_program()
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()
