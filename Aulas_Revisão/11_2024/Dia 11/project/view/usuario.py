from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

from controller.controller_usuario import Controller_Usuario

ui_file = "Aulas_Revisão/11_2024/Dia 11/project/ui/usuario_window.ui"

class UsuarioWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file, self)
        
        self.controller_usuario = Controller_Usuario(self)   
        self.botao_cadastrar.clicked.connect(self.cadastrar)
        self.botao_voltar.clicked.connect(self.voltar)

    def cadastrar(self):
        nome = self.nome.text()
        cpf = self.cpf.text()
        telefone = self.telefone.text()
        senha = self.senha.text()
        confirmar_senha = self.confirmar_senha.text()
        label_error = self.label_error  

        id_usuario = self.controller_usuario.cadastrar(nome, cpf, telefone, senha, confirmar_senha, label_error)
        
    def voltar(self):
        self.controller_usuario.voltar()
