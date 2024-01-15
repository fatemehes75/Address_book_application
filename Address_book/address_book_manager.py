from Contact import Contacts
class AddressBookManager:
    def __init__(self,contact_list):
        self.contact_list = contact_list

    def display(self):
        for contact in self.contact_list:
            print(f"Name: {contact.name}, Phone Number: {contact.phonenumber}, Location: {contact.location}, Email: {contact.email}")

    def add(self, name, phone_number, location, email):
        contact = Contacts(name, phone_number, location, email)
        self.contact_list.append(contact)
        print(f"Contact '{name}' added successfully.")

    def delete(self, name):
        for contact in self.contact_list:
            if contact.name.lower() == name.lower():
                self.contact_list.remove(contact)
                print(f"Contact '{name}' deleted successfully.")
                return
        print(f"Contact '{name}' not found.")

    def search(self, name):
        for contact in self.contact_list:
            if contact.name.lower() == name.lower():
                print(f"Contact found:\nName: {contact.name}, Phone Number: {contact.phonenumber}, Location: {contact.location}, Email: {contact.email}")
                return
        print(f"Contact '{name}' not found.")