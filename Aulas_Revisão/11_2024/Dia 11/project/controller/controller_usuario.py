import mysql.connector
from config.database import Database
from models.usuario import Usuario

class Controller_Usuario:
    def __init__(self, window):
        self.window = window
        # self.db = Database("10.28.2.36", "suporte", "suporte", "biblioteca")
        self.db = Database("localhost", "root", "suporte", "biblioteca")
        self.usuario = None 

    def cadastrar(self, nome_completo, cpf, telefone, senha, confirmar_senha, label_error):
        if nome_completo == '' or cpf == '' or telefone == '' or senha == '' or confirmar_senha == '':
            label_error.setStyleSheet('color: red;')
            label_error.setText("Verifique se todos os campos estão preenchidos!")
        elif senha != confirmar_senha:
            label_error.setStyleSheet('color: orange;')
            label_error.setText("Ambos os campos da senha devem ser iguais!")
        else:
            try:
                print(nome_completo, cpf, telefone, senha, confirmar_senha, label_error)
                self.db.conectar()
                self.usuario = Usuario(self.db.cursor, self.db.conexao)  

                if self.usuario.verificar_usuario(cpf):
                    label_error.setStyleSheet('color: red;')
                    label_error.setText("Usuário já existente!")
                else:
                    self.usuario.cadastrar_usuario(nome_completo, cpf, telefone, senha)
                    label_error.setStyleSheet('color: green;')
                    label_error.setText("Cadastro efetuado com sucesso!")

            except mysql.connector.Error as err:
                print(f"Erro ao conectar ao banco de dados: {err}")
                label_error.setStyleSheet('color: red;')
                label_error.setText("Erro ao conectar ao banco de dados.")
            finally:
                self.db.desconectar()

