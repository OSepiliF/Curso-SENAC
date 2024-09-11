from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

def submitact():
    user = usuario_entry.get()
    passw = senha_entry.get()
    text = texto_entry.get()

    if user == '' or passw == '' or text == '':
        messagebox.showerror('Erro!',"Todos os campos devem ser preenchidos.")
        return

    logintodb(user, passw, text)

def logintodb(user, passw, text):
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
            update_db = 'update usuarios set texto = %s where usuario = %s'
            try:
                cursor.execute(update_db, (text, user))
                db.commit()
                messagebox.showinfo('Sucesso!','Texto atualizado.')
                #abrir tela
            except:
                messagebox.showerror('Erro!','Erro em atualizar o texto.')
        else:
            messagebox.showerror('Erro!','Senha incorreta.')
    else:
        verif_create_user = 'insert into usuarios (usuario, senha, texto) values (%s, %s, %s)'
        try:
            cursor.execute(verif_create_user, (user, passw, text))
            db.commit()
            messagebox.showinfo('Sucesso!','Cadastro Realizado')
            #abrir tela
        except:
            messagebox.showerror('Erro!','Usuário não foi cadastrado.')

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
