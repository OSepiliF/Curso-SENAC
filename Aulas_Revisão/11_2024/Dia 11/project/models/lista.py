class Lista:
    def __init__(self, cursor, conexao):
        self.cursor = cursor
        self.conexao = conexao

    def buscar_meus_livros(self, id_usuario):
        if self.cursor is None:
            raise Exception("Conexão com o banco de dados não foi estabelecida.")
        
        query = """
            SELECT livro.titulo, livro.autor, livro.genero 
            FROM livro
            JOIN emprestimo ON livro.codigo = emprestimo.id_livro
            WHERE emprestimo.id_usuario = %s AND emprestimo.devolvido = 0
        """
        
        self.cursor.execute(query, (id_usuario,))
        result = self.cursor.fetchall()
        return [{"titulo": row[0], "autor": row[1], "genero": row[2]} for row in result]
    

    def verificar_livro(self, titulo, autor, genero):
        if self.cursor is None:
            raise Exception("Conexão com o banco de dados não foi estabelecida.")
        
        query = "SELECT 1 FROM livro WHERE titulo = %s AND autor = %s AND genero = %s"
        self.cursor.execute(query, (titulo, autor, genero))
        resultado = self.cursor.fetchone()
        return resultado is not None

    def buscar_livros_disponiveis(self):
        if self.cursor is None:
            raise Exception("Conexão com o banco de dados não foi estabelecida.")
        
        query = "SELECT titulo, autor, genero FROM livro WHERE usuario IS NULL AND status = 'disponível'"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return [{"titulo": row[0], "autor": row[1], "genero": row[2]} for row in result]
