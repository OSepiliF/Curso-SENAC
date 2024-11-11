from livros import Livros
from usuario import Usuario

class Biblioteca:
    acervo:list[Livros] = []
    @staticmethod
    def emprestar(usuario: Usuario, livros: list[Livros]) -> bool:
        for item in livros:
            if len(usuario.lista_livros) == usuario.max_emprestimo:
                break
            livros.emprestar(usuario)
            usuario.pegar_emprestado(item)
        return True

    @staticmethod
    def devolver(livros: Livros, usuario: Usuario):
        livros.devolv_livro()