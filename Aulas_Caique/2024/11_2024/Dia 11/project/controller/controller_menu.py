class Controller_Menu:
    def __init__(self, window, id_usuario):
        self.window = window  
        self.id_usuario = id_usuario

    def abrir_cadastroLivros(self):
        from view.livro import LivroWindow 
        self.window.close()  
        self.cadastroLivrosJanela = LivroWindow(self.id_usuario)  
        self.cadastroLivrosJanela.show()

    def abrir_emprestimoLivros(self):
        from view.emprestimo import EmprestimoWindow  
        self.window.close()  
        self.emprestimoJanela = EmprestimoWindow(self.id_usuario)  
        self.emprestimoJanela.show()

    def abrir_listaLivros(self):
        from view.lista import ListaWindow 
        self.window.close()
        self.listaLivrosJanela = ListaWindow(self.id_usuario) 
        self.listaLivrosJanela.show() 

    def sair(self):
        self.window.close()  

    