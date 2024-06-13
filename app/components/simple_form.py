# simple_form.py
import tkinter as tk

class SimpleForm(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="blue")  # Llama al constructor de la clase base (tk.Frame)
        self.place(x=150, y=50, width=300, height=100) #  Esto hace que el marco se ajuste al tamaño de su contenido.
        self.create_widgets()

    def create_widgets(self):
        self.entry = tk.Entry(self)
        self.entry.pack(pady=10)

        self.button = tk.Button(self, text="Submit", command=self.on_submit)
        self.button.pack(pady=10)

    def on_submit(self):
        print("Entry content:", self.entry.get())