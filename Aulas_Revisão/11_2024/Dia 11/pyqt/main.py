import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

ui_file = "teste.ui"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file, self)
        self.botao_adicionar.clicked.connect(self.clicked)

    def clicked(self): 
        autor = self.line_Edit_autor.text()
        titulo = self.line_Edit_titulo.text()
        genero = self.line_Edit_genero.text()
        codigo = self.spinBox_codigo.text()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())