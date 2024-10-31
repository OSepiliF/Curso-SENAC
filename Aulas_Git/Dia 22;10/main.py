from biblioteca import Biblioteca
from livros import Livros
from usuario import Usuario
import mysql.connector

conexao = mysql.connector.connect(
    host='10.28.2.36',
    user='suporte',
    password='suporte',
    database='biblioteca'
) 


rafaela = Usuario('Rafaela','123.123.123-45','67999887766')

dom_casmurro = Livros('Dom Casmurro','Machado de Assis', 'Romance',1)
incidente_antares = Livros('Incidente em Antares','Érico Verissimo', 'Ficção distópca',2)
pollyanna = Livros('Poliana','Eleanor H. porter ', 'Literatuara Infantil',3)
almanacão_Monica = Livros('Almanacão da turma da Mônica','Mauricio de Souza', 'Literatura Infantil',4)


dom_casmurro.emprestar_livro(rafaela [dom_casmurro, incidente_antares, pollyanna, almanacão_Monica])

