import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

from controller.controller_livro import Controller_Livro

ui_file = "Aulas_Revisão/11_2024/Dia 11/project/ui/livro_window.ui"

class LivroWindow(QMainWindow):
    def __init__(self, id_usuario):
        super().__init__()
        uic.loadUi(ui_file, self)
        self.id_usuario = id_usuario

        self.controller_livro = Controller_Livro(self, id_usuario)   
        self.botao_cadastrar.clicked.connect(self.cadastrar)
        self.botao_voltar.clicked.connect(self.voltar)

    def cadastrar(self):
        autor = self.autor.text()
        titulo = self.titulo.text()
        genero = self.genero.text()
        codigo = self.codigo.text()
        label_error = self.label_error  

        self.controller_livro.cadastrar(autor, titulo, genero, codigo, label_error)

    def voltar(self):
        self.controller_livro.voltar()

