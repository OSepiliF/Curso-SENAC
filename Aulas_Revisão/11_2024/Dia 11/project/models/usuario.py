import mysql.connector

class Usuario:
    def __init__(self, cursor, conexao):
        self.cursor = cursor  
        self.conexao = conexao  
        
    def verificar_usuario(self, cpf):
        query = "SELECT * FROM usuario WHERE cpf = %s"
        self.cursor.execute(query, (cpf,))
        result = self.cursor.fetchone()
        print('Verificou o Usuário.')  
        return result is not None
        
    def cadastrar_usuario(self, nome_completo, cpf, telefone, senha):
        try:
            query = "INSERT INTO usuario (nome_completo, cpf, telefone, senha) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, (nome_completo, cpf, telefone, senha))
            self.conexao.commit() 
            print('Cadastrou o Usuário.')

        except mysql.connector.Error as err:
            print(f"Erro ao cadastrar usuário: {err}")
            self.conexao.rollback()  
