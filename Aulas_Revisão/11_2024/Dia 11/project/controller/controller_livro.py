import mysql.connector

from config.database import Database
from models.livro import Livro

class Controller_Livro:
    def __init__(self, window, id_usuario):
        self.window = window
        self.id_usuario = id_usuario
        self.db = Database("10.28.2.36", "suporte", "suporte", "biblioteca")
        # self.db = Database("localhost", "root", "suporte", "biblioteca")
        self.livro = None

    def cadastrar(self, autor, titulo, genero, codigo, label_error):
        if autor == '' or titulo == '' or genero == '' or codigo == '':
            label_error.setStyleSheet('color: red;')
            label_error.setText("Verifique se todos os campos estão preenchidos!")
        
        if not codigo.isdigit(): 
            label_error.setStyleSheet('color: red;')
            label_error.setText("O código deve ser numérico!")

        else:
            try:
                self.db.conectar()  
                self.livro = Livro(self.db.cursor, self.db.conexao)

                if self.livro.verificar_livro(codigo):
                    label_error.setStyleSheet('color: red;')
                    label_error.setText("Livro já cadastrado!")

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

    def voltar(self):
        from view.menu import MenuWindow
        self.window.close()  
        self.menuJanela = MenuWindow(self.id_usuario)  
        self.menuJanela.show()