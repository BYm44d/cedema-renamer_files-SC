# button.py
import tkinter as tk

class CustomButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(bg='blue', fg='white', font=('Helvetica', 12))
