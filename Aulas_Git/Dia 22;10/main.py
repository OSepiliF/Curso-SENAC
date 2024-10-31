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

cursor = conexao.cursor()

# insert
cursor.execute('''
    insert into livro (titulo, autor, genero, status, codigo) values 
        ("O pequeno principe","Antoine de Saint-Exupéry","Fábula","Disponivel", 123),
        ("Dom Casmurro","Machado de Assis","Romance","Disponivel", 345),
        ("Poliana","Eleonor H. Porter","Literatura Infantil","Disponivel", 678),
        ("Incidente em Antares","Érico Verissimo", "Ficção distópca","Emprestado", 910),
        ("Almanacão da turma da Mônica","Mauricio de Souza", "Literatura Infantil","Emprestado", 111);
    
    insert into usuario (nome, cpf, telefone) values
        ("Rafaela","12345678910","67991234567"),
        ("Enzo","2312312312","67993234561");
''')

# select
cursor.execute('''
    select * from livro;
    select * from livro join usuario on livro.usuario = usuario.id_usuario;         
''')

#update
cursor.execute('update livro set usuario = 1 where id_livro = 1')

#delete
cursor.execute('delete from livro where id_livro = 2')




conexao.commit()

print(dir(conexao))