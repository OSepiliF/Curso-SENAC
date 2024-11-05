from usuario import Usuario
from main import Database


class Livros():
    def __init__(self, titulo, autor, genero, cod_livro):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.cod_livro = cod_livro
        self.status = 'Disponivel'
        self.usuario = None

    def emprestar_livro(self, usuario: Usuario):
        if self.status != 'Disponivel':
            return "Disponivel para emprestar."
        
        if len(usuario.lista_livros) == usuario.max_emprestimo:
            return False
        
        self.usuario = usuario.nome
        self.status = 'Emprestado'

    def devolv_livro(self):
        if self.status != 'Emprestado':
            return "Não pode ser devolvido."
        
        self.usuario = None
        self.status = 'Disponivel'

    def create(self):
        return 'insert into livro(titulo, autor, genero) values()'
    
    def read(self):
        return 'select * from livro'

class Controller_Livros:
    
    def cadastrar_livro():
        db = Database() 
        db.conectar()   
        livro = Livros()
        livro.create

        db.cursor.execute()
    


    