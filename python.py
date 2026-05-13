import json

contacts = {}

while True:

    print("\n--- CONTACT BOOK ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Save Contacts")
    print("5. Load Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Contact
    if choice == "1":

        name = input("Enter contact name: ")
        number = input("Enter phone number: ")

        contacts[name] = number

        print("Contact added successfully")

    # View Contacts
    elif choice == "2":

        if contacts:

            print("\nSaved Contacts:")

            for name, number in contacts.items():

                print(name, "->", number)

        else:
            print("No contacts found")

    # Search Contact
    elif choice == "3":

        search = input("Enter contact name to search: ")

        if search in contacts:

            print(search, "->", contacts[search])

        else:
            print("Contact not found")

    # Save Contacts to JSON file
    elif choice == "4":

        with open("contacts.json", "w") as file:

            json.dump(contacts, file, indent=4)

        print("Contacts saved successfully")

    # Load Contacts from JSON file
    elif choice == "5":

        try:

            with open("contacts.json", "r") as file:

                contacts = json.load(file)

            print("Contacts loaded successfully")

        except FileNotFoundError:

            print("No saved contacts file found")

    # Exit
    elif choice == "6":

        print("Exiting Contact Book")

        break

    else:

        print("Invalid choice")
