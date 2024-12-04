from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

from controller.controller_login import Controller_Login

ui_file = "Aulas_Revisão/11_2024/Dia 11/project/ui/login_window.ui"

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file, self)

        self.controller_login = Controller_Login(self)  
        self.botao_cadastrar.clicked.connect(self.tela_cadastrar)
        self.botao_login.clicked.connect(self.login)

    def tela_cadastrar(self):
        print('Abrindo tela de cadastro!')
        self.controller_login.tela_cadastrar()  

    def login(self):
        nome = self.nome.text()
        senha = self.senha.text()
        label_error = self.label_error

        self.controller_login.login(nome, senha, label_error)          

