import mysql.connector
          
class Login:
    def __init__(self, cursor, conexao):
        self.cursor = cursor
        self.conexao = conexao

    def verificar_credenciais(self, nome, senha):
        try:
            query = "SELECT id_usuario FROM usuario WHERE nome = %s AND senha = %s"
            self.cursor.execute(query, (nome, senha))
            usuario = self.cursor.fetchone()
            if usuario:
                return usuario[0]  
            return None

        except mysql.connector.Error as err:
            print(f"Erro ao cadastrar usuário: {err}")
            self.conexao.rollback()  