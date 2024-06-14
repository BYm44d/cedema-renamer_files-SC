import tkinter
import tkinter as tk
from tkinter import filedialog
import os
# home_controller.py
class HomeController:
    def __init__(self, view):
        self.view = view
        self.view.boton_send.config(command=self.update_label)
        self.view.boton_select.config(command=self.selected_directory)
        self.init_views()

    def limit_entry(self, *args):
        value = self.var_entrada_extencion.get()
        if len(value) > 4:  # Limitar a 4 caracteres
            self.var_entrada_extencion.set(value[:4])

    def init_views(self):
        self.view.seleccion.config(values=["Incluir Extensión", "Modificar Extensión"])
        self.view.seleccion.set("Incluir Extensión")
        self.view.seleccion.bind('<<ComboboxSelected>>', self.on_combobox_select)
        
        self.var_entrada_extencion = tkinter.StringVar()
        self.var_entrada_extencion.trace_add('write', self.limit_entry)
        self.view.entrada_extencion.config(textvariable=self.var_entrada_extencion)

    def update_label(self):
        # name = self.view.entry.get()
        # self.view.result_label.config(text=f"Hello, {name}!")
        # print("Acurazao")
        print("Acurazao")

    def on_combobox_select(self, event):
        if self.view.seleccion.get() == "Incluir Extensión":
            self.view.entrada_extencion.pack_forget()
        else:
            self.view.entrada_extencion.pack(padx=10, pady=10)

    def listar_archivos(self, directorio):
        # Obtener una lista de todos los archivos en el directorio
        archivos = os.listdir(directorio)

        # Imprimir la lista de archivos
        i = 0
        for archivo in archivos:
            i += 1
            self.view.lista_files.insert(tkinter.END, archivo)
            print(archivo)
        self.view.lista_files.configure(height=i)

    def selected_directory(self):
        directorio = filedialog.askdirectory(initialdir="/home/jeiro/_TALLER-L_/")
        print(directorio)
        self.listar_archivos(directorio)

    