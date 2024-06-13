# # main.py
# import tkinter as tk
# from app.views.home_view import HomeView
# from controllers.home_controller import HomeController

# def main():
#     # Crear y configurar la ventana principal
#     ventana = tk.Tk()
#     ventana.title("Renombrador de Archivos")
#     ventana.geometry("800x500")

#     # Crear la vista principal y el controlador
#     home_view = HomeView(master=ventana)
#     home_controller = HomeController(view=home_view)

#     # Ejecutar el bucle principal de la ventana
#     home_view.mainloop()

# if __name__ == "__main__":
#     main()


# main.py
import tkinter as tk
from components.simple_form import SimpleForm

def main():
    # Crear y configurar la ventana principal
    ventana = tk.Tk()
    ventana.title("Aplicación Simple")
    ventana.geometry("400x200")

    # Crear el formulario simple y agregarlo a la ventana
    simple_form = SimpleForm(master=ventana)
    
    # Ejecutar el bucle principal de la ventana
    ventana.mainloop()

if __name__ == "__main__":
    main()
