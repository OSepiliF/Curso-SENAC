import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

ui_file = "Aulas_Revisão/11_2024/Dia 11/project/ui/login_window.ui"

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file, self)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())