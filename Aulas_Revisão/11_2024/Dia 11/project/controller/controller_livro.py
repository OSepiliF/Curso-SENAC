import mysql.connector

from config.database import Database
from models.livro import Livro

class Controller_Livro:
    def __init__(self, window, id_usuario):
        self.window = window
        self.id_usuario = id_usuario
        # self.db = Database("10.28.2.36", "suporte", "suporte", "biblioteca")
        self.db = Database("localhost", "root", "suporte", "biblioteca")
        self.livro = None

    def cadastrar(self, autor, titulo, genero, codigo, label_error):
        if autor == '' or titulo == '' or genero == '' or codigo == '':
            label_error.setStyleSheet('color: red;')
            label_error.setText("Verifique se todos os campos estão preenchidos!")
            return

        if not codigo.isdigit():
            label_error.setStyleSheet('color: red;')
            label_error.setText("O código deve ser numérico!")
            return

        try:
            self.db.conectar()
            self.livro = Livro(self.db.cursor, self.db.conexao)

            if self.livro.verificar_livro(titulo, autor, genero):
                label_error.setStyleSheet('color: red;')
                label_error.setText("Livro já cadastrado!")

            if self.livro.verificar_codigo(codigo):
                label_error.setStyleSheet('color: red;')
                label_error.setText("Código já existente")
            else:
                self.livro.cadastrar_livro(autor, titulo, genero, codigo)
                label_error.setStyleSheet('color: green;')
                label_error.setText("Livro cadastrado com sucesso!")

        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            label_error.setStyleSheet('color: red;')
            label_error.setText("Erro ao conectar ao banco de dados.")

        finally:
            self.db.desconectar()

    def deletar(self, autor, titulo, genero, codigo, label_error):
        if autor == '' or titulo == '' or genero == '' or codigo == '':
            label_error.setStyleSheet('color: red;')
            label_error.setText("Verifique se todos os campos estão preenchidos!")
            return

        if not codigo.isdigit():
            label_error.setStyleSheet('color: red;')
            label_error.setText("O código deve ser numérico!")
            return

        try:
            self.db.conectar()
            self.livro = Livro(self.db.cursor, self.db.conexao)

            if not self.livro.verificar_livro(titulo, autor, genero):
                label_error.setStyleSheet('color: red;')
                label_error.setText("Livro inexistente")
            else:
                self.livro.deletar_livro(codigo)
                label_error.setStyleSheet('color: green;')
                label_error.setText("Livro deletado com sucesso!")

        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            label_error.setStyleSheet('color: red;')
            label_error.setText("Erro ao conectar ao banco de dados.")

    def voltar(self):
        from view.menu import MenuWindow
        self.window.close()  
        self.menuJanela = MenuWindow(self.id_usuario)  
        self.menuJanela.show()