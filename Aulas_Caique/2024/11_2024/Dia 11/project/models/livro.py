class Livro:
    def __init__(self, cursor, conexao):
        self.cursor = cursor
        self.conexao = conexao

    def verificar_livro(self, titulo, autor, genero):
        query = "SELECT * FROM livro WHERE titulo = %s AND autor = %s AND genero = %s"
        self.cursor.execute(query, (titulo, autor, genero))
        resultado = self.cursor.fetchone()
        return bool(resultado)  
    
    def verificar_codigo(self, codigo):
        query = "SELECT * FROM livro WHERE codigo = %s"
        self.cursor.execute(query, (codigo,))
        resultado = self.cursor.fetchone()
        return bool(resultado)  

    def cadastrar_livro(self, autor, titulo, genero, codigo):
        query = "INSERT INTO livro (autor, titulo, genero, codigo) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(query, (autor, titulo, genero, codigo))
        self.conexao.commit()
        

    def deletar_livro(self, codigo):
        query = "DELETE FROM livro WHERE codigo = %s"
        self.cursor.execute(query, (codigo,))
        self.conexao.commit()
        
