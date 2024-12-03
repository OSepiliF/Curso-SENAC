import mysql.connector
from config.database import Database
from models.lista import Lista
from PyQt5.QtWidgets import QListWidgetItem

class Controller_Lista:
    def __init__(self, window, id_usuario):
        self.window = window
        self.id_usuario = id_usuario
        self.db = Database("10.28.2.36", "suporte", "suporte", "biblioteca")
        # self.db = Database("localhost", "root", "suporte", "biblioteca")
        self.db.conectar() 
        self.lista_model = Lista(self.db.cursor, self.db.conexao)

    def ver_meusLivros(self):
        try:
            livros = self.lista_model.buscar_meus_livros(self.id_usuario)
            self.atualizar_lista(livros)
            
        except Exception as e:
            print(f"Erro ao buscar livros: {e}")

    def ver_livrosDisponiveis(self):
        try:
            livros = self.lista_model.buscar_livros_disponiveis()
            self.atualizar_lista(livros)

        except Exception as e:
            print(f"Erro ao buscar livros disponíveis: {e}")

    def atualizar_lista(self, livros):
        self.window.listWidget.clear()  
        for livro in livros:
            item = QListWidgetItem(
                f"({livro['codigo']}) | Titulo: {livro['titulo']} - Autor: {livro['autor']} - "
                f"Gênero: {livro['genero']} "
            )
            self.window.listWidget.addItem(item)

    def voltar(self):
        from view.menu import MenuWindow
        self.window.close()
        menu_window = MenuWindow(self.id_usuario)
        menu_window.show()
