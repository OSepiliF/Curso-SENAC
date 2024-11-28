import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
  
from view.usuario import UsuarioWindow    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    usuarioJanela = UsuarioWindow()
    usuarioJanela.show()
    sys.exit(app.exec_())
