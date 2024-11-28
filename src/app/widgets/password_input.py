import tkinter as tk

class PasswordInput(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Create a label for password input
        self.label = tk.Label(self.master, text="Password Length:")
        self.label.grid(row=0, column=0, padx=10, pady=10)

        # Create an entry field to input password length
        self.entry = tk.Entry(self.master)
        self.entry.grid(row=0, column=1, padx=10, pady=10)
        self.entry.insert(0, "12")  # Default length

    def get_length(self):
        try:
            length = int(self.entry.get())
            return length
        except ValueError:
            return None

    def set_password(self, password):
        # Update the entry field with the generated password
        self.entry.delete(0, tk.END)
        self.entry.insert(0, password)
