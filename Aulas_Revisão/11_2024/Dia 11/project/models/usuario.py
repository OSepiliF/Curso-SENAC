import mysql.connector

class Usuario:
    def __init__(self, cursor, conexao):
        self.cursor = cursor  
        self.conexao = conexao  

    def validar_cpf(self, cpf):
        cpf = ''.join(filter(str.isdigit, cpf))  
        return len(cpf) == 11  
        
    def verificar_usuario(self, cpf):
        query = "SELECT * FROM usuario WHERE cpf = %s"
        self.cursor.execute(query, (cpf,))
        return self.cursor.fetchone() is not None 
        
    def cadastrar_usuario(self, nome, cpf, telefone, senha):
        if not self.validar_cpf(cpf):
            print("Erro: CPF inválido.")
            return False

        try:
            query = "INSERT INTO usuario (nome, cpf, telefone, senha) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, (nome, cpf, telefone, senha))
            self.conexao.commit() 
            print("Usuário cadastrado com sucesso.")
            return True

        except mysql.connector.Error as err:
            print(f"Erro ao cadastrar usuário: {err}")
            self.conexao.rollback()  
            return False
