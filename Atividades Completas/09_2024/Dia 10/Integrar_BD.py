from tkinter import *
from tkinter import ttk
import mysql.connector

def submitact():
    user = usuario_entry.get()
    passw = senha_entry.get()
    text = texto_entry.get()
  
    print(f"The name entered by you is {user} {passw} {text}")
  
    logintodb(user, passw, text)
 
def logintodb(user, passw, text):
    
    if passw:
        db = mysql.connector.connect(host ="10.28.2.36",
                                     user = 'suporte',
                                     password = 'suporte',
                                     db ="registros_db")
        cursor = db.cursor()
         
        savequery = "SELECT * FROM usuarios"
        update_db = f'UPDATE usuarios SET texto = {text} WHERE usuario = {user}'
        
        try:
            cursor.execute(savequery)
            cursor.execute(update_db, (text, user))
            db.commit()
            myresult = cursor.fetchall()
           
            for x in myresult:
                print(x)
            print("Query Executed successfully")
             
        except mysql.connector.Error as err:
            db.rollback()
            print(f"Error occurred: {err}")
        finally:
            cursor.close()
            db.close()

def abrir_tela_cadastro():
    global usuario_entry, senha_entry, texto_entry
    
    root = Tk()
    root.geometry('400x500')
    root.title('Login')
    root.config(bg='grey18')

    Label(root, text="Preencha os dados abaixo:", font=("Titan One", 18, "bold"), bg='grey18', fg='white').place(relx=0.5, rely=0.15, anchor="center")

    Label(root, text='Usuário', font=('Titan One', 15, "bold"), bg='grey18', fg='white').place(relx=0.5, rely=0.30, anchor="center")
    usuario_entry = Entry(root, font=('Titan One', 15, "bold"))
    usuario_entry.place(relx=0.5, rely=0.35, anchor="center")

    Label(root, text="Senha", font=("Titan One", 15, "bold"), bg='grey18', fg='white').place(relx=0.5, rely=0.45, anchor="center")
    senha_entry = Entry(root, font=("Titan One", 15), show="*")
    senha_entry.place(relx=0.5, rely=0.5, anchor="center")

    Label(root, text="Texto", font=("Titan One", 15, "bold"), bg='grey18', fg='white').place(relx=0.5, rely=0.6, anchor="center")
    texto_entry = Entry(root, font=("Titan One", 15))
    texto_entry.place(relx=0.5, rely=0.65, anchor="center")

    style = ttk.Style()
    style.configure('custom.TButton', font=('Titan One', 12, "bold"), padding=(10.5), anchor="center")
    btn = ttk.Button(root, text="Entrar", command=submitact, style='custom.TButton')
    btn.place(relx=0.5, rely=0.8, anchor="center")

    root.mainloop()

if __name__ == "__main__":
    abrir_tela_cadastro()
