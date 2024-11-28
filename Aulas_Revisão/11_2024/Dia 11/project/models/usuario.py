import mysql.connector

class Usuario:
    def __init__(self, host, user, password, dbname):
        self.host = host
        self.user = user
        self.password = password
        self.dbname = dbname
        self.conexao = None
        self.cursor = None

    def conectar(self):
        try:
            self.conexao = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.dbname
            )
            self.cursor = self.conexao.cursor()

        except mysql.connector.Error:
            print(f"Erro ao conectar ao banco de dados")

    def desconectar(self):
        if self.conexao:
            self.conexao.close()

    def verificar_usuario(self, cpf):
        try:
            self.cursor.execute("SELECT cpf FROM usuario WHERE cpf = %s", (cpf,))
            return self.cursor.fetchone()  
        
        except mysql.connector.Error:
            print(f"Erro ao verificar usuário")

    def cadastrar_usuario(self, nome, cpf, telefone):
        try:
            self.cursor.execute("INSERT INTO usuario (nome, cpf, telefone) VALUES (%s, %s, %s)", 
                                (nome, cpf, telefone))
            self.conexao.commit()

        except mysql.connector.Error:
            print(f"Erro ao cadastrar usuário")
