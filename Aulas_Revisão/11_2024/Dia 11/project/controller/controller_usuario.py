from config.database import Database

class Controller_Usuario:
    def __init__(self):
        self.db = Database("10.28.2.36", "suporte", "suporte", "biblioteca")

    def cadastrar(self):
        nome_completo = self.view.lineEdit_nomecompleto.text()
        cpf = self.view.lineEdit_cpf.text()
        telefone = self.view.lineEdit_telefone.text()
        senha = self.view.lineEdit_senha.text()
        confirmar_senha = self.view.lineEdit_confirmarsenha.text()

        if nome_completo == '' or cpf == '' or telefone == '' or senha == '' or confirmar_senha == '':
            self.view.label_error.setStyleSheet('color: red;')
            self.view.label_error.setText('Verifique se todos os campos estão preenchidos!')

        elif senha != confirmar_senha:
            self.view.label_error.setStyleSheet('color: orange;')
            self.view.label_error.setText('Ambos os campos da senha devem ser iguais!')

        else:
            self.db.conectar()

            if self.db.verificar_usuario(cpf):
                self.view.label_error.setStyleSheet('color: red;')
                self.view.label_error.setText('Usuário já existente!')

            else:
                self.db.cadastrar_usuario(nome_completo, cpf, telefone)
                self.view.label_error.setStyleSheet('color: green;')
                self.view.label_error.setText('Cadastro Efetuado com Sucesso!')

                self.view.lineEdit_nomecompleto.clear()
                self.view.lineEdit_cpf.clear()
                self.view.lineEdit_telefone.clear()
                self.view.lineEdit_senha.clear()
                self.view.lineEdit_confirmarsenha.clear()

            self.db.desconectar()

Controller_Usuario.__name__ = 'Controller_Usuario'
