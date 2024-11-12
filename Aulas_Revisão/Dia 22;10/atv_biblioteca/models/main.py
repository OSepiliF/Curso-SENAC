import mysql.connector
from usuario import Usuario
from livros import Livros

class Database:
    def __init__(self, host, user, password, database):
        self.host = host 
        self.user = user
        self.password = password
        self.database = database
        self.conexao = None
        self.cursor = None

    def conectar(self):
        self.conexao = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database
            )
        
        if self.conexao.is_connected():
            print("Conectado")

        self.cursor = self.conexao.cursor()

    def desconectar(self):
        self.conexao.close()    

Database.__name__ = 'Database'    