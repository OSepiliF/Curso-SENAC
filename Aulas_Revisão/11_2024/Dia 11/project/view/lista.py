from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem

from controller.controller_lista import Controller_Lista

ui_file = "Aulas_Revisão/11_2024/Dia 11/project/ui/lista_window.ui"

class ListaWindow(QMainWindow):
    def __init__(self, id_usuario):
        super().__init__()
        uic.loadUi(ui_file, self)

        self.controller_emprestimo = Controller_Lista(self, id_usuario)
        self.botao_meusLivros.clicked.connect(self.ver_meusLivros)
        self.botao_disponiveis.clicked.connect(self.ver_livrosDisponiveis)
        self.botao_voltar.clicked.connect(self.voltar)

    def ver_meusLivros(self):
        self.controller_emprestimo.ver_meusLivros()

    def ver_livrosDisponiveis(self):
        self.controller_emprestimo.ver_livrosDisponiveis()

    def voltar(self):
        self.controller_emprestimo.voltar()