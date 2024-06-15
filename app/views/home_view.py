# home_view.py
import tkinter
import tkinter as tk
from tkinter import ttk

class HomeView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="blue")
        self.master = master
        self.pack(fill=tkinter.BOTH, expand=True)
        self.create_widgets()
        self.files_list()

    def create_widgets(self):
        frame1 = tkinter.Frame(self, bg="red", width=100)
        frame1.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)

        frame_extension = tkinter.Frame(frame1, bg="orange", width=100)
        frame_extension.pack(fill=tkinter.X)
        frame_extension.pack_propagate(False)  # Evita que el widget cambie su tamaño para ajustarse a sus hijos
        frame_extension.config(height=100)  # Establece el alto del widget

        etiqueta = tkinter.Label(frame_extension, text="Extensión", bg="orange", fg="white", font=("Helvetica", 10, "bold")) # Crea una 
        etiqueta.pack(padx=10, pady=10) # Margin en x,y
        self.seleccion = ttk.Combobox(frame_extension)
        self.seleccion.pack()

        self.entrada_extencion = tkinter.Entry(frame_extension)
        self.entrada_extencion.pack_forget()

        etiqueta = tkinter.Label(frame1, text="La variable de numeración es: {num}", bg="red", fg="white", font=("Helvetica", 10, "bold")) # Crea una 
        etiqueta.pack(padx=10, pady=10) # Margin en x,y

        self.seleccion_renameType = ttk.Combobox(frame1)
        self.seleccion_renameType.pack(padx=10, pady=10)
        
        frame_nameInput = tkinter.Frame(frame1, bg="green", width=100)
        frame_nameInput.pack(fill=tkinter.X)
        frame_nameInput.columnconfigure(0, weight=1)
        frame_nameInput.columnconfigure(1, weight=1)
        frame_nameInput.columnconfigure(2, weight=1)

        self.entrada_newName = tkinter.Entry(frame_nameInput)
        self.entrada_newName.grid(row=0, column=1, padx=10, pady=10)

        self.entrada_SustiName = tkinter.Entry(frame_nameInput)
        self.entrada_SustiName.grid(row=0, column=0, padx=10, pady=10)
        self.entrada_SustiName.grid_forget()

        self.etiqueta_señal = tkinter.Label(frame_nameInput, text="-->", bg="green", fg="black", font=("Helvetica", 10, "bold"))
        self.etiqueta_señal.grid(row=0, column=1)
        self.etiqueta_señal.grid_forget()

        self.entrada_SustiName2 = tkinter.Entry(frame_nameInput)
        self.entrada_SustiName2.grid(row=0, column=2, padx=10, pady=10)
        self.entrada_SustiName2.grid_forget()

        self.boton_rename = tkinter.Button(frame1, text="Renombrar")
        self.boton_rename.pack(padx=10, pady=10)

    def files_list(self):
        frame2 = tkinter.Frame(self, bg="blue", width=200)
        frame2.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)

        etiqueta = tkinter.Label(frame2, text="Lista de archivos", bg="blue", fg="white", font=("Helvetica", 10, "bold")) # Crea una 
        etiqueta.pack(padx=10, pady=10) # ALGO SIMILAR A MARGIN
        self.lista_files = tkinter.Listbox(frame2, height=0)
        self.lista_files.pack()

        self.boton_select = tkinter.Button(frame2, text="Seleccionar Carpeta")
        self.boton_select.pack(padx=10, pady=10)

        self.boton_clear = tkinter.Button(frame2, text="Limpiar Lista")
        self.boton_clear.pack(padx=10)