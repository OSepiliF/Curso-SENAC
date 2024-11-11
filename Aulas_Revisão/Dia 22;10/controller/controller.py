from livros import Livro
from main import Database

class Controller_Livro:
   def cadastrar_livro(self):
      db = Database("10.28.2.39","suporte","suporte","biblioteca")
      db.conectar()
      
      livros = Livro("um autor ai","Um titulo ai", "trans?", "15" )

      db.cursor.execute(livros.create())
      db.conexao.commit()
      db.desconectar()

   def procurar_Livro(self):
      procurar = Database("10.28.2.39","suporte","suporte","biblioteca")
      procurar.conectar()

      procurar.cursor.execute('Select * from livro where codigo = 15')
      print(procurar.cursor.fetchall())
      procurar.desconectar()
   
   def atualizar_Livro(self):
      atualizar = Database("10.28.2.39","suporte","suporte","biblioteca")
      atualizar.conectar()


      atualizar.cursor.execute("update livro set titulo = 'um titulo com update' where codigo = 15")
      atualizar.conexao.commit()
      atualizar.desconectar()

   
   def excluir_Livro(self):
      excluindo = Database("10.28.2.39","suporte","suporte","biblioteca")
      excluindo.conectar()

      excluindo.cursor.execute("delete from livro where codigo = 15")
      excluindo.conexao.commit()
      excluindo.desconectar()

      
op = Controller_Livro()
op.procurar_Livro()