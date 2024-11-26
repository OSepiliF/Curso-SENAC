import mysql.connector
from models.usuario import Usuario
from models.livros import Livros

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
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.conexao.cursor()

    def desconectar(self):
        if self.cursor:
            self.cursor.close()
            
        if self.conexao:
            self.conexao.close()

    def verificar_usuario(self, cpf):
        query = "SELECT * FROM usuarios WHERE cpf = %s"
        self.cursor.execute(query, (cpf,))
        result = self.cursor.fetchone()  
        return result

    def cadastrar_usuario(self, nome_completo, cpf, telefone):
        query = "INSERT INTO usuarios (nome_completo, cpf, telefone) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (nome_completo, cpf, telefone))
        self.conexao.commit()

Database.__name__ = 'Database'    