import tkinter as tk
from tkinter import messagebox
from .gui import PasswordGeneratorApp
from .config import CONFIG

def main():
    # Create the main Tkinter window
    root = tk.Tk()
    root.title(CONFIG["APP_NAME"])
    root.geometry(CONFIG["WINDOW_SIZE"])

    # Initialize and run the Password Generator application
    app = PasswordGeneratorApp(root)
    app.mainloop()

if __name__ == "__main__":
    main()
