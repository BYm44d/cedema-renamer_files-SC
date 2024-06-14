# main.py
import tkinter as tk
from views.home_view import HomeView
from controllers.home_controller import HomeController

def main():
    # Crear y configurar la ventana principal
    ventana = tk.Tk()
    ventana.title("Renombrador de Archivos")
    ventana.geometry("800x500")

    # Crear la vista principal y el controlador
    home_view = HomeView(master=ventana)
    home_controller = HomeController(view=home_view)

    # Ejecutar el bucle principal de la ventana
    home_view.mainloop()


if __name__ == "__main__":
    main()

    # Este bloque asegura que main() se ejecutará solo si el script main.py se ejecuta directamente. Si otro script importa main.py, main() no se ejecutará automáticamente, permitiendo que main.py sea utilizado como un módulo sin efectos secundarios indeseados.
