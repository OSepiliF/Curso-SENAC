import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from view.login import LoginWindow 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    loginJanela = LoginWindow()
    loginJanela.show()
    sys.exit(app.exec_())

    print('Abrindo tela de login.')