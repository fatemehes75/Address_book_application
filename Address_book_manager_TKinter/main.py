import tkinter as tk
from address_book_gui import AddressBookGUI

if __name__ == "__main__":
    root = tk.Tk()
    app = AddressBookGUI(root)
    root.mainloop()
