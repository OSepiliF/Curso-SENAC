class Livro:
    def __init__(self, cursor, conexao):
        self.cursor = cursor
        self.conexao = conexao

    def verificar_livro(self, codigo=None, titulo=None, autor=None):
        if codigo:
            query = "SELECT * FROM livro WHERE codigo = %s"
            self.cursor.execute(query, (codigo,))
            resultado = self.cursor.fetchone()
            if resultado:  
                return True
        
        if titulo and autor:
            query = "SELECT * FROM livro WHERE titulo = %s AND autor = %s"
            self.cursor.execute(query, (titulo, autor))
            resultado = self.cursor.fetchone()
            if resultado:  
                return True
        return False  


    def cadastrar_livro(self, autor, titulo, genero, codigo):
        query = "INSERT INTO livro (autor, titulo, genero, codigo) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(query, (autor, titulo, genero, codigo))
        self.conexao.commit()  
