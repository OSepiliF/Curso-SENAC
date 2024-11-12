import mysql.connector
from livros import Livros
from usuario import Usuario

class Biblioteca:
    def __init__(self, titulo, autor, genero, status, codigo):
        self.livros_atributos = None
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.status = status
        self.codigo = codigo

    def livrando_livro(self):
        self.livros_atributos = mysql.Dataframe({
        'titulo':self.titulo,
        'autor':self.autor,
        'genero':self.genero,
        'status':self.status,
        'codigo':self.codigo
        })
        
    def emprestimo_livro(self):
        if self.status != 'Disponivel':
            return
        
        self.usuario = Usuario.nome
        self.status = 'Emprestado'

    def devolver_livro(self):
        if self.status != 'Emprestado':
            return
        
        self.usuario = None
        self.status = 'Disponivel'
