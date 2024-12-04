from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

from controller.controller_menu import Controller_Menu  

ui_file = "Aulas_Revisão/11_2024/Dia 11/project/ui/menu_window.ui"

class MenuWindow(QMainWindow):
    def __init__(self, id_usuario):
        super().__init__()
        uic.loadUi(ui_file, self)
        self.id_usuario = id_usuario
        
        self.controller_menu = Controller_Menu(self, id_usuario)  
        self.botao_listaLivros.clicked.connect(self.abrir_listaLivros)
        self.botao_cadastroLivros.clicked.connect(self.abrir_cadastroLivros)
        self.botao_emprestimoLivros.clicked.connect(self.abrir_emprestimoLivros)  
        self.botao_sair.clicked.connect(self.sair)

    def abrir_listaLivros(self):
        self.controller_menu.abrir_listaLivros()
        
    def abrir_cadastroLivros(self):
        self.controller_menu.abrir_cadastroLivros()
        
    def abrir_emprestimoLivros(self):
        self.controller_menu.abrir_emprestimoLivros()
        
    def sair(self):
        self.controller_menu.sair() 
