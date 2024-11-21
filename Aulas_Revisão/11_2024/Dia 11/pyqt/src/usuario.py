import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

ui_file = "Aulas_Revisão/11_2024/Dia 11/pyqt/ui/usuario_window.ui"

class UsuarioWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file, self)
        self.botao_cadastrar.clicked.connect(self.cadastrar)
        self.botao_cancelar.clicked.connect(self.cancelar)

    def cadastrar(self): 
        self.label_error.setText('')
        nome_completo = self.lineEdit_nomecompleto.text()
        cpf = self.lineEdit_cpf.text()
        telefone = self.lineEdit_telefone.text()
        senha = self.lineEdit_senha.text()
        confirmar_senha = self.lineEdit_confirmarsenha.text()

        if nome_completo == '' or cpf == '' or telefone == '' or senha == '' or confirmar_senha == '':
            self.label_error.setStyleSheet('color: red;')
            self.label_error.setText('Verifique se todos os campos estão preenchidos!')

        elif senha != confirmar_senha:
            self.label_error.setStyleSheet('color: orange;')
            self.label_error.setText('Ambos os campos da senha devem ser iguais!')

        else:
            self.label_error.setStyleSheet('color: green;')
            self.label_error.setText('Cadastro Efetuado.')
            print(f"Nome Completo: {nome_completo}")
            print(f"CPF: {cpf}")
            print(f"Telefone: {telefone}")
            print(f"Senha: {senha}")

    def cancelar(self):
        print('Cancelando...')
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UsuarioWindow()
    window.show()
    sys.exit(app.exec_())
