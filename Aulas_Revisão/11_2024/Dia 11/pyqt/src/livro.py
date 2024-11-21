import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

ui_file = "Aulas_Revisão/11_2024/Dia 11/pyqt/ui/main_window.ui"

class LivroWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file, self)
        self.botao_cadastrar.clicked.connect(self.cadastrar)
        self.botao_cancelar.clicked.connect(self.cancelar)

    def cadastrar(self): 
        self.label_error.setText('')
        autor = self.lineEdit_autor.text()
        titulo = self.lineEdit_titulo.text()
        genero = self.lineEdit_genero.text()
        codigo = self.lineEdit_codigo.text()
        
        if autor == '' or titulo == '' or genero == '' or codigo == '':
            self.label_error.setStyleSheet('color: red;')
            self.label_error.setText('Verifique se todos os campos estão preenchidos!')
        
        else:
            self.label_error.setStyleSheet('color: green;')
            self.label_error.setText('Cadastro Efetuado.')
            print(f"Autor: {autor}")
            print(f"Título: {titulo}")
            print(f"Gênero: {genero}")
            print(f"Código: {codigo}")

    def cancelar(self):
        print('Cancelando...')
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LivroWindow()
    window.show()
    sys.exit(app.exec_())