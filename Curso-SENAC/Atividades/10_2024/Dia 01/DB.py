import sqlite3

# conect = sqlite3.connect('banco_dados.db')

# cursor = conect.cursor()

# cursor.execute('''
#     CREATE TABLE usuario(
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 nome TEXT NOT NULL,
#                 email TEXT NOT NULL               
#     )
# ''')

# conect.commit()
# conect.close()

# -----------------------------------------------------

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conect = None
        self.cursor = None
    
    def conectar(self):
        self.conect = sqlite3.connect(self.db_name)
        self.cursor = self.conect.cursor()

    def commit(self):
        if self.conect:
            self.conect.commit()

    def executar(self, query, parametros = None):
        if parametros:
            self.cursor.execute(query, parametros)
        else:
            self.cursor.execute(query)
        self.conect.commit()

    def fetchAll(self):
        return self.cursor.fetchall()

db = Database('banco_dados.db')
db.conectar()