from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

def verif():
    if usuario.get() == '' or senha.get() == '':
        messagebox.showerror('Erro', 'Preencha todas as opções.')
    elif senha.get() == usuario.get():
        messagebox.showerror("Erro!", "Senha e usuário não podem ser iguais.")
    else:
        if usuario.get() != usuario:
             messagebox.showerror('Aviso!', 'Não há usuários com essas informações')
        else:
            messagebox.showinfo("Sucesso!", f"O usuário {usuario.get()} foi cadastrado.")
        logintodb(usuario,senha)

def logintodb(usuario, senha):
    global db
    try:
        if senha:
            db = mysql.connector.connect(host="10.28.2.36",
                                         user='suporte',
                                         password='suporte',
                                         database="registros")
        else:
            db = mysql.connector.connect(host="10.28.2.36",
                                         user='suporte',
                                         database="registros")
            
        cursor = db.cursor()

        savequery = "SELECT * FROM STUDENT"

        cursor.execute(savequery)
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
        print("Query Executed successfully")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        
    finally:
        cursor.close()
        db.close()

def abrir_tela_cadastro():
    global usuario, senha
    
    root = Tk()
    root.geometry('400x400')
    root.title('Login')
    root.config(bg='grey18')

    Label(root, text="Preencha os dados abaixo:", font=("Titan One", 18, "bold"), bg='grey18', fg='white').place(relx=0.5, rely=0.15, anchor="center")

    Label(root, text='Usuário', font=('Titan One', 15, "bold"), bg='grey18', fg='white').place(relx=0.5, rely=0.33, anchor="center")
    usuario = Entry(root, font=('Titan One', 15, "bold"))
    usuario.place(relx=0.5, rely=0.4, anchor="center")

    Label(root, text="Senha", font=("Titan One", 15, "bold"), bg='grey18', fg='white').place(relx=0.5, rely=0.53, anchor="center")
    senha = Entry(root, font=("Titan One", 15), show="*")
    senha.place(relx=0.5, rely=0.60, anchor="center")

    style = ttk.Style()
    style.configure('custom.TButton', font=('Titan One', 12, "bold"), padding=(10.5), anchor="center")
    btn = ttk.Button(root, text="Entrar", command=verif, style='custom.TButton')
    btn.place(relx=0.5, rely=0.8, anchor="center")

    root.mainloop()

if __name__ == "__main__":
    abrir_tela_cadastro()