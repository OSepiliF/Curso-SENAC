import mysql.connector

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
        print('Conectou no Banco de Dados.')

    def desconectar(self):
        if self.cursor:
            self.cursor.close()
            
        if self.conexao:
            self.conexao.close()
            print('Desconectou do Banco de Dados.')