import tkinter as tk
from tkinter import simpledialog
from address_book_manager import AddressBookManager
from Contact import Contacts
from data import data_contact


class AddressBookGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Address Book")

        self.contacts_bank = []
        for key, value in data_contact.items():
            new_contact = Contacts(key, value['Phonenumber'], value['Location'], value['Email'])
            self.contacts_bank.append(new_contact)

        self.address_book_manager = AddressBookManager(self.contacts_bank)

        self.create_widgets()

    def create_widgets(self):
        # Display Contacts Button
        display_button = tk.Button(self.master, text="Display Contacts", command=self.display_contacts)
        display_button.pack(pady=10)

        # Add Contact Button
        add_button = tk.Button(self.master, text="Add Contact", command=self.add_contact)
        add_button.pack(pady=10)

        # Delete Contact Button
        delete_button = tk.Button(self.master, text="Delete Contact", command=self.delete_contact)
        delete_button.pack(pady=10)

        # Search Contact Button
        search_button = tk.Button(self.master, text="Search Contact", command=self.search_contact)
        search_button.pack(pady=10)

        # Exit Button
        exit_button = tk.Button(self.master, text="Exit", command=self.master.destroy)
        exit_button.pack(pady=10)

    def display_contacts(self):
        self.address_book_manager.display()

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter name:")
        phone_number = simpledialog.askstring("Input", "Enter phone number:")
        location = simpledialog.askstring("Input", "Enter location:")
        email = simpledialog.askstring("Input", "Enter email:")

        self.address_book_manager.add(name, phone_number, location, email)

    def delete_contact(self):
        name = simpledialog.askstring("Input", "Enter name to delete:")
        self.address_book_manager.delete(name)

    def search_contact(self):
        name = simpledialog.askstring("Input", "Enter name to search:")
        self.address_book_manager.search(name)