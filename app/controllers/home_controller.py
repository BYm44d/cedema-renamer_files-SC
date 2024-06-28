import tkinter
import tkinter as tk
from tkinter import filedialog
import os
from tkinter import messagebox
from utils.helpers import Helper

class HomeController(Helper):
    def __init__(self, view):
        super().__init__()
        self.view = view
        self.list_files = []
        self.new_list_files = []
        self.view.boton_rename.config(command=self.renamer_files)
        self.view.boton_select.config(command=self.selected_directory)
        self.view.boton_clear.config(command=self.clear_list)
        self.init_views()

    def limit_entry(self, *args):
        value = self.var_entrada_extencion.get()
        self.chanel_extencion(value[:4])
        if len(value) > 4:  # Limitar a 4 caracteres
            self.var_entrada_extencion.set(value[:4])

    def init_views(self):
        self.view.seleccion.config(values=["Incluir Extensión", "Modificar Extensión"])
        self.view.seleccion.set("Incluir Extensión")
        self.view.seleccion.bind('<<ComboboxSelected>>', self.on_combobox_select)
        
        self.var_entrada_extencion = tkinter.StringVar()
        self.var_entrada_extencion.trace_add('write', self.limit_entry)
        self.view.entrada_extencion.config(textvariable=self.var_entrada_extencion)

        self.view.seleccion_renameType.config(values=["Renombrar", "Sustituir"])
        self.view.seleccion_renameType.set("Renombrar")
        self.view.seleccion_renameType.bind('<<ComboboxSelected>>', self.renamer_type)

        self.valor_entry = tkinter.StringVar() # ESTA ES UNA VARIABLE DE CONTROL 'valor_entry'
        self.valor_entry.trace_add('write', self.view_change_name)
        self.view.entrada_newName.config(textvariable=self.valor_entry)

        self.valor_SustiName = tkinter.StringVar()
        self.valor_SustiName.trace_add('write', self.Sustit_Name)
        self.view.entrada_SustiName.config(textvariable=self.valor_SustiName)

        
        self.valor_SustiName2 = tkinter.StringVar()
        self.valor_SustiName2.trace_add('write', self.Sustit_Name)
        self.view.entrada_SustiName2.config(textvariable=self.valor_SustiName2)

    def renamer_files(self):
        i = 0
        for n in self.list_files:
            if os.path.exists(f'{self.directorio}/{self.new_list_files[i]}'):
                if self.view.seleccion_renameType.get() == "Renombrar":
                    messagebox.showerror("Error, conflicto", f'Ya existe un archivo con este nombre: {self.new_list_files[i]}, procura que los nombres sean diferentes!')
                    break
            else:
                os.rename(f'{self.directorio}/{n}', f'{self.directorio}/{self.new_list_files[i]}')
            i += 1
        messagebox.showinfo("Messaje", "Renombramiento Finalizado!")
        self.reset_values()
        self.listar_archivos()

    def on_combobox_select(self, event):
        if self.view.seleccion.get() == "Incluir Extensión":
            self.view.entrada_extencion.pack_forget()
        else:
            self.view.entrada_extencion.pack(padx=10, pady=10)

    def listar_archivos(self):
        # Obtener una lista de todos los archivos en el directorio
        archivos = os.listdir(self.directorio)

        # Imprimir la lista de archivos
        i = 0
        self.list_files = []
        self.view.lista_files.delete(0, tkinter.END) # LIMPIAR LISBOX
        for archivo in archivos:
            i += 1
            self.view.lista_files.insert(tkinter.END, archivo)
            self.list_files.append(archivo)
        self.view.lista_files.configure(height=i)

    def selected_directory(self):
        self.directorio = filedialog.askdirectory(initialdir="/home/jeiro/_TALLER-L_/")
        self.listar_archivos()

    def view_change_name(self, *args):
        value = self.valor_entry.get()
        i = 0
        self.new_list_files = []
        for n in self.list_files:
            i += 1
            self.view.lista_files.delete(0)
            extension = n.split('.')[-1]
            output_num = value.replace('{num}', f'{i:02d}')
            output_casec = output_num.replace('{cased}', self.implement_casec())
            self.view.lista_files.insert(tkinter.END, f'{output_casec}.{extension}')
            self.new_list_files.append(f'{output_casec}.{extension}')

    def renamer_type(self, event):
        if self.view.seleccion_renameType.get() == "Renombrar":
            print("Renombrar")
            self.view.entrada_newName.grid(row=0, column=1, padx=10, pady=10)
            self.view.entrada_SustiName.grid_forget()
            self.view.etiqueta_señal.grid_forget()
            self.view.entrada_SustiName2.grid_forget()
        else:
            print("Sustituir")
            self.view.entrada_newName.grid_forget()
            self.view.entrada_SustiName.grid(row=0, column=0, padx=10, pady=10)
            self.view.etiqueta_señal.grid(row=0, column=1)
            self.view.entrada_SustiName2.grid(row=0, column=2, padx=10, pady=10)

    def Sustit_Name(self, *args):
        value = self.valor_SustiName.get()
        value2 = self.valor_SustiName2.get()

        self.new_list_files = []
        i = 0
        for n in self.list_files:
            i += 1
            self.view.lista_files.delete(0)
            final_rename = n.replace(value, value2)
            output_num = final_rename.replace('{num}', f'{i:02d}')
            self.view.lista_files.insert(tkinter.END, output_num)
            self.new_list_files.append(output_num)

    def clear_list(self):
        self.view.lista_files.delete(0, tkinter.END)
        self.list_files = []
        self.view.lista_files.configure(height=0)

    def chanel_extencion(self, value):
        other_list = []
        if self.new_list_files:
            other_list = self.new_list_files
        else:
            other_list = self.list_files
        self.new_list_files = []
        for n in other_list:
            self.view.lista_files.delete(0)
            extension = n.split('.')[-1]
            extension_modify = n.replace(extension, value)
            self.view.lista_files.insert(tkinter.END, extension_modify)
            self.new_list_files.append(extension_modify)

    def reset_values(self):
        self.view.entrada_newName.delete(0, tkinter.END)
        self.view.entrada_SustiName.delete(0, tkinter.END)
        self.view.entrada_SustiName2.delete(0, tkinter.END)
        self.view.entrada_extencion.delete(0, tkinter.END)