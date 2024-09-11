from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

def confirmar_login():
    user = usuario_entry.get()
    passw = senha_entry.get()

    if user == '' or passw == '':
        messagebox.showerror('Erro!',"Todos os campos devem ser preenchidos.")
        return

    logintodb(user, passw)

def logintodb(user, passw):
    db = mysql.connector.connect(host="10.28.2.36",
                                user='suporte',
                                password='suporte',
                                db="registros_db")

    # db = mysql.connector.connect(host="localhost",
    #                             user='root',
    #                             password='suporte',
    #                             db="registros_db")
    
    cursor = db.cursor()

    verif_exist = 'select * from usuarios where usuario = %s'
    cursor.execute(verif_exist, (user,))
    result = cursor.fetchone()

    if result:
        if result[2] == passw:
            preecher_text = Toplevel()
            preecher_text.geometry('400x200')
            preecher_text.title('Login')
            preecher_text.config(bg='grey18')

            Label(preecher_text, text="Texto", font=("Titan One", 15, "bold"), bg='grey18', fg='white').place(relx=0.5, rely=0.2, anchor="center")
            texto_entry = Entry(preecher_text, font=("Titan One", 15))
            texto_entry.place(relx=0.5, rely=0.4, anchor="center")

            confirmar_text = ttk.Button(preecher_text, text="Inserir", command='confirmar_login', style='custom.TButton')
            confirmar_text.place(relx=0.5, rely=0.7, anchor="center")
        else:
            messagebox.showerror('Erro!','Senha incorreta.')

def abrir_login():
    global usuario_entry, senha_entry
    
    root = Tk()
    root.geometry('400x500')
    root.title('Login')
    root.config(bg='grey18')

    Label(root, text="Preencha os dados abaixo:", font=("Titan One", 18, "bold"), bg='grey18', fg='white').place(relx=0.5, rely=0.15, anchor="center")
    Label(root, text="Caso não possua um usuário\n Clique em cadastrar", font=("Titan One", 9, "bold"), bg='grey18', fg='white').place(relx=0.5, rely=0.8, anchor="center")


    Label(root, text='Usuário', font=('Titan One', 15, "bold"), bg='grey18', fg='white').place(relx=0.5, rely=0.30, anchor="center")
    usuario_entry = Entry(root, font=('Titan One', 15, "bold"))
    usuario_entry.place(relx=0.5, rely=0.35, anchor="center")

    Label(root, text="Senha", font=("Titan One", 15, "bold"), bg='grey18', fg='white').place(relx=0.5, rely=0.45, anchor="center")
    senha_entry = Entry(root, font=("Titan One", 15), show="*")
    senha_entry.place(relx=0.5, rely=0.5, anchor="center") 

    style = ttk.Style()
    style.configure('custom.TButton', font=('Titan One', 12, "bold"), padding=(10.5), anchor="center")

    btn_login = ttk.Button(root, text="Entrar", command=confirmar_login, style='custom.TButton')
    btn_login.place(relx=0.5, rely=0.65, anchor="center")

    btn_cadastrar = ttk.Button(root, text="Cadastrar", command='abrir_cadastro', style='custom.TButton')
    btn_cadastrar.place(relx=0.5, rely=0.9, anchor="center")

    root.mainloop()

if __name__ == "__main__":
    abrir_login()
