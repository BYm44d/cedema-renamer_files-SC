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
        self.seleccion.set("Incluir Extensión")
        self.seleccion.pack()

        self.entrada_extencion = tkinter.Entry(frame_extension, textvariable='patata')
        self.entrada_extencion.pack_forget()

        # ANCHOR ENTRADA DE TEXTO
        etiqueta = tkinter.Label(frame1, text="Las variables para la identificacion \n del los archivos renombrados son {num} o {letter}", bg="red", fg="white", font=("Helvetica", 10, "bold")) # Crea una 
        etiqueta.pack(padx=10, pady=10) # ALGO SIMILAR A MARGIN
        # Entrada
        # valor_entry = "hola mundo"
        
        self.valor_entry = tkinter.StringVar() # ESTA ES UNA VARIABLE DE CONTROL 'valor_entry'
        self.valor_entry.trace_add('write', self.limit_entry2)
        self.entrada_newName = tkinter.Entry(frame1, textvariable=self.valor_entry)
        # self.entrada_newName.bind('<Key>', self.limit_entry2)
        self.entrada_newName.pack(padx=10, pady=10)

        # ANCHOR BUTTON
        self.boton_send = tkinter.Button(frame1, text="Renombrar")
        self.boton_send.pack(padx=10, pady=10)

    def limit_entry2(self, *args):
        print("hhh")
        # value = self.valor_entry.get()
        # print(value)
        
    def files_list(self):
        frame2 = tkinter.Frame(self, bg="blue", width=200)
        frame2.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)

        etiqueta = tkinter.Label(frame2, text="Lista de archivos", bg="blue", fg="white", font=("Helvetica", 10, "bold")) # Crea una 
        etiqueta.pack(padx=10, pady=10) # ALGO SIMILAR A MARGIN
        self.lista_files = tkinter.Listbox(frame2, height=0)
        self.lista_files.pack()

        # ANCHOR BUTTON
        self.boton_select = tkinter.Button(frame2, text="Seleccionar Carpeta")
        self.boton_select.pack(padx=10, pady=10)