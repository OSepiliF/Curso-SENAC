import mysql.connector
from atividade import connect_sql
from biblioteca import biblioteca

class usuario:
    def __init__(self,nome,cpf,telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    def usando_usuario(self):
        self.usuario_atributos = mysql.DataFrame({
            'nome':self.nome,
            'cpf':self.cpf,
            'telefone':self.telefone
            })