from livros import Livros
from main import Database

class Controller_Livro:
   def cadastrar_livro(self):
      db = Database("10.28.2.36","suporte","suporte","biblioteca")
      db.conectar()

      livros = Livros("Autor","Titulo", "Genero", "2121" )

      db.cursor.execute(livros.create())
      db.conexao.commit()
      db.desconectar()
   
   def procurar_livro(self):
      procurar = Database("10.28.2.36","suporte","suporte","biblioteca")
      procurar.conectar()

      livros = Livros("Autor","Titulo", "Genero", "2121" )

      procurar.cursor.execute(livros.read())
      print(procurar.cursor.fetchall())
      procurar.desconectar()


   def atualizar_livro(self):
      atualizar = Database("10.28.2.36","suporte","suporte","biblioteca")
      atualizar.conectar()

      livros = Livros("Autor","Titulo", "Genero", "2121" )

      atualizar.cursor.execute(livros.update())
      atualizar.conexao.commit()
      atualizar.desconectar()


   def excluir_livro(self):
      excluindo = Database("10.28.2.36","suporte","suporte","biblioteca")
      excluindo.conectar()

      livros = Livros("Autor","Titulo", "Genero", "2121" )

      excluindo.cursor.execute(livros.delete())
      excluindo.conexao.commit()
      excluindo.desconectar()

op = Controller_Livro()
op.cadastrar_livro()
op.procurar_livro()
