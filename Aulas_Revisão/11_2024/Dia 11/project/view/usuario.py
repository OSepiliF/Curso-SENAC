import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from controller.controller_usuario import Controller_Usuario

ui_file = "Aulas_Revisão/11_2024/Dia 11/pyqt/ui/usuario_window.ui"

class UsuarioWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file, self) 
        self.botao_cadastrar.clicked.connect(self.cadastrar)
        self.botao_cancelar.clicked.connect(self.cancelar)

        self.controller = Controller_Usuario(self)

    def cadastrar(self):
        self.controller.cadastrar()  

    def cancelar(self):
        print('Cancelando...') 
        self.close()

UsuarioWindow.__name_ = 'UsuarioWindow'

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UsuarioWindow()
    window.show()
    sys.exit(app.exec_())
