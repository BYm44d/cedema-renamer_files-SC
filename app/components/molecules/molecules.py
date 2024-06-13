# form.py
import tkinter as tk
from components.atoms.atoms import CustomButton

class Form(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.label = tk.Label(self, text="Name:")
        self.entry = tk.Entry(self)
        self.submit_button = CustomButton(self, text="Submit")
        self.label.pack()
        self.entry.pack()
        self.submit_button.pack()
