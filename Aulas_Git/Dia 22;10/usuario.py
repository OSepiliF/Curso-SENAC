class Usuario:
    max_emprestimo = 3

    def __init__(self, nome_user, cpf, telefone):
        self.nome_user = nome_user
        self.cpf = cpf
        self.telefone = telefone
        self.lista_livros = []

    def pegar_emprestado(self, livros):
        if len(self.lista_livros) >= self.max_emprestimo:
            return "Limite de emprestimo atingido."
        
        self.lista_livros.append(livros.titulo)