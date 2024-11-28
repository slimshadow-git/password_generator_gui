import tkinter as tk
from tkinter import messagebox
from .widgets.password_input import PasswordInput
from .widgets.generate_button import GenerateButton
from .styles import apply_styles
from ..utils.password_generator import generate_password
from ..utils.validators import validate_password_length

class PasswordGeneratorApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.configure_gui()
        self.create_widgets()

    def configure_gui(self):
        apply_styles(self.master)

    def create_widgets(self):
        self.password_input = PasswordInput(self.master)
        self.password_input.grid(row=0, column=0, padx=20, pady=20)

        self.generate_button = GenerateButton(self.master, command=self.generate_password)
        self.generate_button.grid(row=1, column=0, padx=20, pady=20)

    def generate_password(self):
        length = self.password_input.get_length()
        
        if not validate_password_length(length):
            messagebox.showerror("Invalid Input", "Password length must be between 8 and 20 characters.")
            return
        
        password = generate_password(length)
        self.password_input.set_password(password)
