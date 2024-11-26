from config.database import Database
from models.livros import Livros

class Controller_Livro:
   def cadastrar_livro(self):
      db = Database("10.28.2.36","suporte","suporte","biblioteca")
      db.conectar()

      livros = Livros("Autor","Titulo", "Genero", "2121" )

      db.cursor.execute(livros.create())
      db.conexao.commit()
      db.desconectar()
   
   
   def procurar_livro(self):
      db = Database("10.28.2.36","suporte","suporte","biblioteca")
      db.conectar()

      livros = Livros("Autor","Titulo", "Genero", "2121" )

      db.cursor.execute(livros.read())
      print(db.cursor.fetchall())
      db.desconectar()


   def atualizar_livro(self):
      db = Database("10.28.2.36","suporte","suporte","biblioteca")
      db.conectar()

      livros = Livros("Autor","Titulo", "Genero", "2121" )

      db.cursor.execute(livros.update())
      db.conexao.commit()
      db.desconectar()


   def excluir_livro(self):
      db = Database("10.28.2.36","suporte","suporte","biblioteca")
      db.conectar()

      livros = Livros("Autor","Titulo", "Genero", "2121" )

      db.cursor.execute(livros.delete())
      db.conexao.commit()
      db.desconectar()

Controller_Livro.__name__ = "Controler_Livro"

# op = Controller_Livro()
# op.cadastrar_livro()
# op.procurar_livro()
