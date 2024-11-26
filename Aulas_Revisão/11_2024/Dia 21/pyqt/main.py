import mysql.connector

# ////////////////////////////////////////////////////////////////////////////////////////////////
class Database:
    def __init__(self, host, user, password, database):
        self.host = host 
        self.user = user
        self.password = password
        self.database = database
        self.conexao = None
        self.cursor = None

    def conectar(self):
        self.conexao = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.conexao.cursor()

    def desconectar(self):
        if self.conexao:
            self.conexao.close()

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params)
        self.conexao.commit()

# ////////////////////////////////////////////////////////////////////////////////////////////////
class Livros:
    def __init__(self, autor, titulo, genero, codigo, status="Disponivel"):
        self.autor = autor
        self.titulo = titulo
        self.genero = genero
        self.codigo = codigo
        self.status = status

    def create(self):
        return "INSERT INTO livros (autor, titulo, genero, codigo, status) VALUES (%s, %s, %s, %s, %s)"

    def update(self):
        return "UPDATE livros SET status = %s WHERE codigo = %s"

    def delete(self):
        return "DELETE FROM livros WHERE codigo = %s"

    def read(self):
        return "SELECT * FROM livros WHERE titulo = %s"

# ////////////////////////////////////////////////////////////////////////////////////////////////
class Controller_Livro:
    def cadastrar_livro(self, autor, titulo, genero, codigo):
        db = Database("10.28.2.36", "suporte", "suporte", "biblioteca")
        db.conectar()

        livro = Livros(autor, titulo, genero, codigo)
        query = livro.create()
        params = (livro.autor, livro.titulo, livro.genero, livro.codigo, livro.status)
        db.execute_query(query, params)

        db.desconectar()

    def procurar_livro(self, titulo):
        db = Database("10.28.2.36", "suporte", "suporte", "biblioteca")
        db.conectar()

        livro = Livros("", titulo, "", "")
        query = livro.read()
        db.cursor.execute(query, (titulo,))
        result = db.cursor.fetchall()

        if result:
            for row in result:
                print(row)
        else:
            print("Livro não encontrado.")

        db.desconectar()

    def atualizar_livro(self, codigo, novo_status):
        db = Database("10.28.2.36", "suporte", "suporte", "biblioteca")
        db.conectar()

        livro = Livros("", "", "", codigo, novo_status)
        query = livro.update()
        params = (livro.status, livro.codigo)
        db.execute_query(query, params)

        db.desconectar()

    def excluir_livro(self, codigo):
        db = Database("10.28.2.36", "suporte", "suporte", "biblioteca")
        db.conectar()

        livro = Livros("", "", "", codigo)
        query = livro.delete()
        db.execute_query(query, (livro.codigo,))

        db.desconectar()

# Testando as funcionalidades
if __name__ == '__main__':
    controller = Controller_Livro()

    # Cadastrar livros
    controller.cadastrar_livro("Autor A", "Título A", "Ficção", "2121")
    controller.cadastrar_livro("Autor B", "Título B", "Não-ficção", "2122")

    # Procurar livros
    controller.procurar_livro("Título A")

    # Atualizar livro
    controller.atualizar_livro("2121", "Emprestado")

    # Excluir livro
    controller.excluir_livro("2122")
