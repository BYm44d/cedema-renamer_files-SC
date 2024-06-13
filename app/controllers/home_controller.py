# home_controller.py
from app.components.organisms.dialog import Dialog

class HomeController:
    def __init__(self, view):
        self.view = view
        self.view.open_dialog_button.config(command=self.handle_open_dialog)

    def handle_open_dialog(self):
        dialog = Dialog(self.view)
        dialog.grab_set()
