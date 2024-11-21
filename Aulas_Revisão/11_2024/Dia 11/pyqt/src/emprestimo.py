import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from main import Database

ui_file = "Aulas_Revisão/11_2024/Dia 11/pyqt/ui/emprestimo_window.ui"

class EmprestimoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file, self)
        self.botao_cadastrar.clicked.connect(self.cadastrar)
        self.botao_cancelar.clicked.connect(self.cancelar)

    def cadastrar(self): 
        self.label_error.setText('')
        nome_completo = self.lineEdit_nomecompleto.text()
        senha = self.lineEdit_senha.text()
        titulo = self.lineEdit_titulo.text()

        if nome_completo == '' or senha == '' or titulo == '':
            self.label_error.setStyleSheet('color: red;')
            self.label_error.setText('Verifique se todos os campos estão preenchidos!')

        else:
            db = Database("10.28.2.36","suporte","suporte","biblioteca")
            db.conectar()

            # Verifica se o livro está disponível
            db.cursor.execute(f"SELECT status FROM livros WHERE titulo = '{titulo}'")
            result = db.cursor.fetchone()

            if result and result[0] == 'Disponivel':
               
                db.cursor.execute(f"UPDATE livros SET status = 'Emprestado' WHERE titulo = '{titulo}'")
                db.conexao.commit()

                self.label_error.setStyleSheet('color: green;')
                self.label_error.setText('Livro Emprestado com Sucesso!')
            else:
                self.label_error.setStyleSheet('color: red;')
                self.label_error.setText('Livro Não Disponível!')

            db.desconectar()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmprestimoWindow()
    window.show()
    sys.exit(app.exec_())