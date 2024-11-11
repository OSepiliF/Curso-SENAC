import mysql.connector
class Database:
    def __init__(self, host, user, password, database):
        self.host = host 
        self.user = user
        self.password = password
        self.database = database
        self.conexao = None
        self.cursor = None

    def conectar(self):
            self.conexao = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database
                )
            
            if self.conexao.is_connected():
                print("Conectado")

            self.cursor = self.conexao.cursor()

    def desconectar(self):
        self.conexao.close()        



# meu_servidor = Database("10.28.2.39",'suporte','suporte','biblioteca')
# meu_servidor.conectar()
# meu_servidor.cursor.execute("insert into livro(titulo, autor, genero, status,codigo) values ('o pequeno principe', 'Enzo','fantasia', 'disponivel',1)")

# print(vars(meu_servidor))

# # cursor.execute("insert into livro(titulo, autor, genero, status,codigo) values ('o pequeno principe', 'Enzo','fantasia', 'disponivel',1)")
# # cursor.execute("insert into usuario(nome,cpf,telefone) values ('Rafaela','1234567891011','67912378666')")
# # cursor.execute("update livro set usuario = 1 where id_livro = 1")
# # cursor.execute("delete from livro where id_livro = 1")

# # conexao.commit()
# # print(dir(conexao))