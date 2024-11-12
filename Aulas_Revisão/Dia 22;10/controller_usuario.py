from usuario import Usuario
from main import Database

class Controller_Usuario:
    def cadastrar_usuario(self):
        db = Database("10.28.2.36","suporte","suporte","biblioteca")
        db.conectar()

        usuario = Usuario("Um jão aí","12345678910", "67999887766")

        db.cursor.execute(usuario.create())
        db.conexao.commit()
        db.desconectar()


    def procurar_usuario(self):
        db = Database("10.28.2.36","suporte","suporte","biblioteca")
        db.conectar()

        usuario = Usuario("Um jão aí","12345678910", "67999887766")

        db.cursor.execute(usuario.read())
        print(db.cursor.fetchall())
        db.desconectar()


    def atualizar_usuario(self):
        db = Database("10.28.2.36","suporte","suporte","biblioteca")
        db.conectar()

        usuario = Usuario("Um jão aí","12345678910", "67999887766")

        db.cursor.execute(usuario.update())
        db.conexao.commit()
        db.desconectar()


    def excluir_usuario(self):
        db = Database("10.28.2.36","suporte","suporte","biblioteca")
        db.conectar()

        usuario = Usuario("Um jão aí","12345678910", "67999887766")
        
        db.cursor.execute(usuario.delete())
        db.conexao.commit()
        db.desconectar()

op = Controller_Usuario()
op.cadastrar_usuario()
op.procurar_usuario()