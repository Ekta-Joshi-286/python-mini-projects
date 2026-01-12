# Contact Book Program

contacts = {}  # Empty dictionary to store contact info

def add_contact():
    name = input("Enter name: ").title()
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts[name] = {'phone': phone, 'email': email}
    print(f"✅ {name} added successfully!")

def update_contact():
    name = input("Enter the name to update: ").title()
    if name in contacts:
        phone = input("Enter new phone: ")
        email = input("Enter new email: ")
        contacts[name] = {'phone': phone, 'email': email}
        print(f"🔄 {name}'s details updated!")
    else:
        print("Contact not found!")

def delete_contact():
    name = input("Enter the name to delete: ").title()
    if name in contacts:
        del contacts[name]
        print(f"❌ {name} deleted!")
    else:
        print("Contact not found!")

def search_contact():
    name = input("Enter the name to search: ").title()
    if name in contacts:
        print(f"\nName: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print("Contact not found!")

def display_all():
    if not contacts:
        print("No contacts found!")
    else:
        print("\n📇 All Contacts (A–Z):")
        for name in sorted(contacts.keys()):
            print(f"{name} - Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")

# Main menu loop
while True:
    print("\n------ CONTACT BOOK ------")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Delete Contact")
    print("4. Search Contact")
    print("5. Show All Contacts")
    print("6. Exit")

    choice = input("Enter your choice (1–6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        update_contact()
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        search_contact()
    elif choice == '5':
        display_all()
    elif choice == '6':
        print("👋 Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
