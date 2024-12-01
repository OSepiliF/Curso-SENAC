import mysql.connector

class Emprestimo:
    def __init__(self, cursor, conexao):
        self.cursor = cursor
        self.conexao = conexao

    def verificar_limite_emprestimos(self, id_usuario):
        query = "SELECT COUNT(*) FROM emprestimo WHERE id_usuario = %s AND devolvido = false"
        self.cursor.execute(query, (id_usuario,))
        return self.cursor.fetchone()[0]

    def verificar_disponibilidade(self, titulo):
        query = "SELECT status FROM livro WHERE titulo = %s"
        self.cursor.execute(query, (titulo,))
        livro = self.cursor.fetchone()
        return livro and livro[0] == 'disponível'

    def registrar_emprestimo(self, id_usuario, titulo, autor):
        try:
            query_livro = "SELECT id_livro FROM livro WHERE titulo = %s AND autor = %s AND status = 'disponível'"
            self.cursor.execute(query_livro, (titulo, autor))
            livro = self.cursor.fetchone()

            if not livro:
                return False  

            id_livro = livro[0]

            query_emprestimos_ativos = "SELECT COUNT(*) FROM emprestimo WHERE id_usuario = %s AND devolvido = 0"
            self.cursor.execute(query_emprestimos_ativos, (id_usuario,))
            livros_emprestados = self.cursor.fetchone()[0]

            if livros_emprestados >= 3:
                return False 
  
            query_emprestimo = "INSERT INTO emprestimo (id_usuario, id_livro) VALUES (%s, %s)"
            self.cursor.execute(query_emprestimo, (id_usuario, id_livro))

            query_update_livro = "UPDATE livro SET status = 'emprestado' WHERE id_livro = %s"
            self.cursor.execute(query_update_livro, (id_livro,))

            self.conexao.commit() 
            return True  
        except mysql.connector.Error as e:
            self.conexao.rollback()  
            print(f"Erro ao registrar empréstimo: {e}")
            return False 

    def devolver(self, id_usuario, codigo_livro):
        try:
            query_devolver = """
                UPDATE emprestimo 
                SET devolvido = true 
                WHERE id_usuario = %s AND id_livro = %s AND devolvido = false
            """
            self.cursor.execute(query_devolver, (id_usuario, codigo_livro))

            query_update_livro = "UPDATE livro SET status = 'disponível' WHERE id_livro = %s"
            self.cursor.execute(query_update_livro, (codigo_livro,))

            self.conexao.commit() 

        except mysql.connector.Error as e:
            self.conexao.rollback() 
            print(f"Erro ao devolver livro: {e}")
