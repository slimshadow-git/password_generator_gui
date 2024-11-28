import tkinter as tk

class GenerateButton(tk.Button):
    def __init__(self, master=None, command=None):
        super().__init__(master, text="Generate Password", command=command)
        self.master = master
        self.configure(width=20, height=2)
