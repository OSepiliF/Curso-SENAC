from DB import Database

class Usuario:
    def __init__(self, db_name):
        self.db = Database(db_name)
        self.db.conectar()

    # CREATE
    def CriarUser(self, nome, email):
        query = 'INSERT INTO usuario (nome, email) VALUES (?, ?)'
        try:
            self.db.executar(query, (nome, email))
            self.db.commit()
        except Exception as err:
            print(f"Erro ao criar usuário: {err}")

    # READ
    def ListarUser(self):
        query = 'SELECT * FROM usuario'
        try:
            self.db.executar(query)
            return self.db.fetchAll()
        except Exception as err:
            print(f"Erro ao listar usuários: {err}")
            return []

    # UPDATE
    def AtualizarUser(self, id, novo_nome=None, novo_email=None):
        query = 'UPDATE usuario SET'
        parametros = []

        if novo_nome:
            query += ' nome = ?'
            parametros.append(novo_nome)
        if novo_email:
            if parametros:
                query += ','
            query += ' email = ?'
            parametros.append(novo_email)
        query += ' WHERE id = ?'
        
        parametros.append(id)
        
        try:
            self.db.executar(query, tuple(parametros))
            self.db.commit()
        except Exception as err:
            print(f"Erro ao atualizar usuário: {err}")

    # DELETE
    def DeletUser(self, id):
        query = 'DELETE FROM usuario WHERE id = ?'
        try:
            self.db.executar(query, (id,))
            self.db.commit()
        except Exception as err:
            print(f"Erro ao deletar usuário: {err}")

user = Usuario('banco_dados.db')