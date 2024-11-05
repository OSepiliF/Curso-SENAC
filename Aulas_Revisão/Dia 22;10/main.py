from biblioteca import Biblioteca
from livros import Livros
from usuario import Usuario
import mysql.connector

# conexao = mysql.connector.connect(
#     host='10.28.2.36',
#     user='suporte',
#     password='suporte',
#     database='biblioteca'
# ) 

# cursor = conexao.cursor()

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

        self.cursor = None
        self.conexao = None

    def conectar(self):
        self.conexao = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database
        )

        self.cursor = self.conexao.cursor()

    def desconectar(self):
        self.conexao.close()


pessoa = Database('10.28.2.36','suporte','suporte','biblioteca')
pessoa.conectar()
pessoa.cursor.execute("select * from livro")
print(pessoa.cursor.fetchall())