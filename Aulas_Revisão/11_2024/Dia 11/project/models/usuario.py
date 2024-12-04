import mysql.connector

class Usuario:
    def __init__(self, cursor, conexao):
        self.cursor = cursor  
        self.conexao = conexao  

    def validar_cpf(self, cpf):
        return 

    def verificar_usuario(self, nome, cpf):
        if nome:
            query = "SELECT * FROM usuario WHERE nome = %s"
            self.cursor.execute(query, (nome,))

        elif cpf:
            query = "SELECT * FROM usuario WHERE cpf = %s"
            self.cursor.execute(query, (cpf,))

        else:
            return False
        return self.cursor.fetchone() is not None

        
    def cadastrar_usuario(self, nome, cpf, telefone, senha):
        if not cpf.isdigit() or len(cpf) != 11:
            print("Erro: CPF inválido.")
            return False
        
        try:
            query = "INSERT INTO usuario (nome, cpf, telefone, senha) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, (nome, cpf, telefone, senha))
            self.conexao.commit()
            print("Usuário cadastrado com sucesso.")
            return True
        
        except mysql.connector.Error as e:
            print(f"Erro ao cadastrar usuário: {e}")
            self.conexao.rollback()
            return False

            
