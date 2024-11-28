from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from controller.controller_usuario import Controller_Usuario

ui_file = "Aulas_Revisão/11_2024/Dia 11/project/ui/usuario_window.ui"

class UsuarioWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file, self)
        
        self.controller = Controller_Usuario(self)   
        self.botao_cadastrar.clicked.connect(self.cadastrar)
        self.botao_cancelar.clicked.connect(self.cancelar)

    def cadastrar(self):
        nome_completo = self.nome_completo.text()
        cpf = self.cpf.text()
        telefone = self.telefone.text()
        senha = self.senha.text()
        confirmar_senha = self.confirmar_senha.text()
        label_error = self.label_error  

        self.controller.cadastrar(nome_completo, cpf, telefone, senha, confirmar_senha, label_error)

    def cancelar(self):
        self.controller.cancelar()
