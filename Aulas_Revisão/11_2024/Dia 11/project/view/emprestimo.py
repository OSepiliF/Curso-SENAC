from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from controller.controller_emprestimo import Controller_Emprestimo

ui_file = "Aulas_Revisão/11_2024/Dia 11/project/ui/emprestimo_window.ui"

class EmprestimoWindow(QMainWindow):
    def __init__(self, id_usuario):
        super().__init__()
        uic.loadUi(ui_file, self)

        self.controller_emprestimo = Controller_Emprestimo(self, id_usuario) 
        self.botao_pegar.clicked.connect(self.pegar_emprestimo)
        self.botao_devolver.clicked.connect(self.devolver_emprestimo)
        self.botao_voltar.clicked.connect(self.voltar)

    def pegar_emprestimo(self):
        titulo = self.titulo.text()
        autor = self.autor.text()   
        genero = self.genero.text()
        label_error = self.label_error  

        self.controller_emprestimo.pegar_emprestimo(titulo, autor, genero, label_error)

    def devolver_emprestimo(self):
        titulo = self.titulo.text()  
        autor = self.autor.text()    
        genero = self.genero.text()
        label_error = self.label_error  

        self.controller_emprestimo.devolver_emprestimo(titulo, autor, genero, label_error)

    def voltar(self):
        self.controller_emprestimo.voltar()
