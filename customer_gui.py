"""
GUI of the customer module
Don't forget external dependencies:

sudo apt-get install python3-tk tk-dev

See https://stackoverflow.com/questions/5459444/tkinter-python-may-not-be-configured-for-tk
"""
from tkinter import Tk, Label, Button, Entry, messagebox

from customer_database import Customer


class CustomerGUI:
    """
    GUI of the customer module
    """

    def __init__(self) -> None:
        """
        Initialize the GUI
        """
        self.customer = Customer()
        self.customer.create_table()
        self.window = Tk()
        self.window.title("Customer")
        self.window.geometry("400x200")
        self.window.resizable(True, True)
        self.window.configure(bg="#52e07c")
        self.label_id = Label(self.window, text="ID")
        self.label_id.grid(row=0, column=0, padx=10, pady=10)
        self.entry_id = Entry(self.window)
        self.entry_id.grid(row=0, column=1, padx=10, pady=10)

        self.label_email = Label(self.window, text="Email")
        self.label_email.grid(row=1, column=0, padx=10, pady=10)
        self.entry_email = Entry(self.window)
        self.entry_email.grid(row=1, column=1, padx=10, pady=10)

        self.button_insert = Button(self.window, text="Insert", command=self.insert)
        self.button_insert.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.window.mainloop()

    def insert(self) -> None:
        """
        Insert a new customer in the database
        """
        try:
            customer_id = int(self.entry_id.get())
            email = self.entry_email.get()
            self.customer.insert(customer_id, email)
            messagebox.showinfo("Success", "Customer inserted")
        except Exception as e:
            messagebox.showerror("Error", str(e))


gui = CustomerGUI()
