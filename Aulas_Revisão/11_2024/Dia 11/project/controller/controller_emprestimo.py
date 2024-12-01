from models.emprestimo import Emprestimo
from models.livro import Livro
from config.database import Database
import mysql.connector

class Controller_Emprestimo:
    def __init__(self, window, id_usuario):
        self.id_usuario = id_usuario
        self.db = Database("localhost", "root", "suporte", "biblioteca")
        self.window = window  

    def pegar_emprestimo(self, titulo, autor, genero, label_error):
        if titulo == '' or autor == '':
            label_error.setStyleSheet('color: red;')
            label_error.setText("O título e o autor são obrigatórios para pegar o empréstimo!")

        try:
            self.db.conectar()
            self.emprestimo = Emprestimo(self.db.cursor, self.db.conexao)

            livros_emprestados = self.emprestimo.verificar_limite_emprestimos(self.id_usuario)
            
            if livros_emprestados >= 3:
                label_error.setStyleSheet('color: red;')
                label_error.setText("Você já tem 3 livros emprestados. Devolva um para pegar outro.") 

            livro_model = Livro(self.db.cursor, self.db.conexao)
            
            livro_existe = livro_model.verificar_livro(titulo, autor, genero)
            
            if livro_existe: 
                if self.emprestimo.verificar_disponibilidade(titulo):  
                   
                    sucesso_emprestimo = self.emprestimo.registrar_emprestimo(self.id_usuario, titulo, autor)
                    
                    if sucesso_emprestimo:
                        label_error.setStyleSheet('color: green;')
                        label_error.setText("Empréstimo realizado com sucesso!")
                    else:
                        label_error.setStyleSheet('color: red;')
                        label_error.setText("Erro ao realizar o empréstimo. Tente novamente mais tarde.")
                else:
                    label_error.setStyleSheet('color: red;')
                    label_error.setText("O livro não está disponível para empréstimo.")
            else:
                label_error.setStyleSheet('color: red;')
                label_error.setText("Livro não encontrado ou não disponível para empréstimo.")

        except mysql.connector.Error as e:
            label_error.setStyleSheet('color: red;')
            label_error.setText("Erro ao conectar ao banco de dados.")
            print(f"Erro no banco de dados: {e}")

        finally:
            self.db.desconectar()

    def devolver_emprestimo(self, titulo, autor, genero, label_error):
        if titulo == '' or autor == '' or genero == '':
            label_error.setStyleSheet('color: red;')
            label_error.setText("O título, o autor e o gênero são obrigatórios para devolver o livro!")
            
        try:
            self.db.conectar()
            self.emprestimo = Emprestimo(self.db.cursor, self.db.conexao)

            query = """
                SELECT livro.codigo 
                FROM livro 
                JOIN emprestimo ON livro.id_livro = emprestimo.id_livro
                WHERE livro.titulo = %s 
                AND livro.autor = %s 
                AND livro.genero = %s 
                AND emprestimo.id_usuario = %s 
                AND emprestimo.devolvido = 0
            """
            self.emprestimo.cursor.execute(query, (titulo, autor, genero, self.id_usuario))
            livro = self.emprestimo.cursor.fetchone()

            if livro:
                codigo = livro[0]
                self.emprestimo.devolver(self.id_usuario, codigo)
                label_error.setStyleSheet('color: green;')
                label_error.setText("Livro devolvido com sucesso!")

            else:
                label_error.setStyleSheet('color: red;')
                label_error.setText("Você não tem esse livro emprestado ou ele já foi devolvido.")

        except mysql.connector.Error as e:
            label_error.setStyleSheet('color: red;')
            label_error.setText("Erro ao conectar ao banco de dados.")
            print(f"Erro no banco de dados: {e}")

        finally:
            self.db.desconectar()

    def voltar(self):
        from view.menu import MenuWindow
        self.window.close()
        menu_window = MenuWindow(self.id_usuario)
        menu_window.show()