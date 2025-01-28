import mysql.connector

from config.database import Database
from models.login import Login

class Controller_Login:
    def __init__(self, window):
        self.window = window
        # self.db = Database("10.28.2.36", "suporte", "suporte", "biblioteca")
        self.db = Database("localhost", "root", "suporte", "biblioteca")
        self.usuario = None
    
    def login(self, nome, senha, label_error):
        if nome == '' or senha == '':  
            label_error.setStyleSheet('color: red;')
            label_error.setText("Nome e senha não podem estar vazios!")
            return

        try:
            self.db.conectar()
            self.usuario = Login(self.db.cursor, self.db.conexao)

            id_usuario = self.usuario.verificar_credenciais(nome, senha)

            if id_usuario:  
                label_error.setStyleSheet('color: green;')
                label_error.setText("Login realizado com sucesso!")
                self.abrir_menu(id_usuario) 
                
            else:
                label_error.setStyleSheet('color: red;')
                label_error.setText("Nome de usuário ou senha incorretos!")

        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            label_error.setStyleSheet('color: red;')
            label_error.setText("Erro ao conectar ao banco de dados.")

        finally:
            self.db.desconectar()

    def tela_cadastrar(self):
        from view.usuario import UsuarioWindow
        self.window.close() 
        self.usuarioJanela = UsuarioWindow() 
        self.usuarioJanela.show()

    def abrir_menu(self, id_usuario):
        from view.menu import MenuWindow
        self.window.close()  
        self.menuJanela = MenuWindow(id_usuario)  
        self.menuJanela.show()  
