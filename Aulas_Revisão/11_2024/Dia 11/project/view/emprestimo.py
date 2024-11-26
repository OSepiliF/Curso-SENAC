import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from config.database import Database

ui_file = "Aulas_Revisão/11_2024/Dia 11/pyqt/ui/emprestimo_window.ui"

class EmprestimoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file, self)
        self.botao_cadastrar.clicked.connect(self.cadastrar)
        self.botao_cancelar.clicked.connect(self.cancelar)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmprestimoWindow()
    window.show()
    sys.exit(app.exec_())