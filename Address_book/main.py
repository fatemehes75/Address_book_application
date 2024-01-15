from Contact import Contacts
from data import data_contact
from address_book_manager import AddressBookManager

contacts_bank = []

# Creating contacts bank using data from data.py
for key, value in data_contact.items():
    new_contact = Contacts(key, value['Phonenumber'], value['Location'], value['Email'])
    contacts_bank.append(new_contact)

# Creating an instance of AddressBookManager class
address_book_manager = AddressBookManager(contacts_bank)

while True:
    print("\nOptions:")
    print("1. Display Contacts")
    print("2. Add Contact")
    print("3. Delete Contact")
    print("4. Search Contact")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        address_book_manager.display()
    elif choice == '2':
        address_book_manager.add(input("Enter name: "), input("Enter phone number: "), input("Enter location: "),
                                 input("Enter email: "))
    elif choice == '3':
        address_book_manager.delete(input("Enter name to delete: "))
    elif choice == '4':
        address_book_manager.search(input("Enter name to search: "))
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
