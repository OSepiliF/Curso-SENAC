from tkinter import *
from tkinter import ttk, messagebox, PhotoImage
import mysql.connector

def confirmar_login():
    global passw
    user = usuario_entry.get()
    passw = senha_entry.get()

    if user == '' or passw == '':
        messagebox.showerror('Erro!', "Todos os campos devem ser preenchidos.")
        return

    login_db(user, passw)

def login_db(user, passw):
    global tela_login
    try:
        # db = mysql.connector.connect(host="localhost",
        #                              user='root',
        #                              password='suporte',
        #                              db="registros_db")   

        db = mysql.connector.connect(host="10.28.2.36",
                                     user='suporte',
                                     password='suporte',
                                     db="registros_db")

        cursor = db.cursor()

        verif_exist = 'select * from usuarios where usuario = %s'
        cursor.execute(verif_exist, (user,))
        result = cursor.fetchone()

        print(result)  

        if result:
            if result[2] == passw:
                tela_login = Toplevel()
                tela_login.geometry('400x200')
                tela_login.title('Digite o texto')
                tela_login.config(bg='grey18')

                Label(tela_login, text="Texto", font=("Titan One", 15, "bold"), bg='grey18', fg='white').place(relx=0.5, rely=0.2, anchor="center")
                texto_entry = Entry(tela_login, font=("Titan One", 15))
                texto_entry.place(relx=0.5, rely=0.4, anchor="center")

                style = ttk.Style()
                style.configure('custom.TButton', font=('Titan One', 12, "bold"), padding=(10.5), anchor="center")

                text_btn = ttk.Button(tela_login, text="Inserir", command=lambda: inserir_texto(user, texto_entry.get(), tela_login), style='custom.TButton')
                text_btn.place(relx=0.5, rely=0.7, anchor="center")
            else:
                messagebox.showerror('Erro!', 'Senha incorreta.')
        else:
            messagebox.showerror('Erro!', 'Esse usuário não existe.')

    except mysql.connector.Error as err:
        messagebox.showerror('Erro!', f'Erro ao conectar ao banco de dados: {err}')

    finally:
        cursor.close()
        db.close()

def inserir_texto(user, text, tela_login):
    try:
        # db = mysql.connector.connect(host="localhost",
        #                              user='root',
        #                              password='suporte',
        #                              db="registros_db")   

        db = mysql.connector.connect(host="10.28.2.36",
                                     user='suporte',
                                     password='suporte',
                                     db="registros_db")
        cursor = db.cursor()
        confirmar_text = 'update usuarios set texto = %s where usuario = %s'
        cursor.execute(confirmar_text, (text, user))
        db.commit()
        messagebox.showinfo('Sucesso!', 'Texto atualizado.')
    except mysql.connector.Error as err:
        messagebox.showerror('Erro!', f'Erro ao atualizar texto: {err}')
    finally:
        cursor.close()
        db.close()
        
        abrir_usuario = Toplevel()
        abrir_usuario.geometry('400x500')
        abrir_usuario.title('Informações do Usuário')
        abrir_usuario.config(bg='grey18')

        img = PhotoImage(file="Imagem_BD\\User_Anônimo.png")
        img_label = Label(abrir_usuario, image=img, bg='grey18')
        img_label.place(relx=0.5, rely=0.26, anchor="center")
        img_label.image = img

        Label(abrir_usuario, text=f"Usuário: {user}", font=("Titan One", 18, "bold"), bg='grey18', fg='white').place(relx=0.5, rely=0.55, anchor="center")
        Label(abrir_usuario, text=f"Senha: {passw}", font=("Titan One", 18, "bold"), bg='grey18', fg='white').place(relx=0.5, rely=0.65, anchor="center")
        Label(abrir_usuario, text=f"Texto: {text}", font=("Titan One", 18, "bold"), bg='grey18', fg='white').place(relx=0.5, rely=0.75, anchor="center")
        
        btn_voltar = ttk.Button(abrir_usuario, text="Voltar", command=abrir_usuario.destroy, style='custom.TButton')
        btn_voltar.place(relx=0.5, rely=0.9, anchor="center")
        tela_login.destroy()

def confirmar_cadastro():
    user = usuario_entry.get()
    passw = senha_entry.get()
    passw_confirm = confirm_senha_entry.get()

    if user == '' or passw == '' or passw_confirm == '':
        messagebox.showerror('Erro!', "Todos os campos devem ser preenchidos.")
        return

    if passw != passw_confirm:
        messagebox.showerror('Erro!', "As senhas não coincidem.")
        return

    if passw == user:
        messagebox.showerror('Erro!', "A senha não pode ser igual ao nome de usuário.")
        return

    try:
        # db = mysql.connector.connect(host="localhost",
        #                              user='root',
        #                              password='suporte',
        #                              db="registros_db")   

        db = mysql.connector.connect(host="10.28.2.36",
                                     user='suporte',
                                     password='suporte',
                                     db="registros_db")
        cursor = db.cursor()

        verif_exist = 'SELECT * FROM usuarios WHERE usuario = %s'
        cursor.execute(verif_exist, (user,))
        result = cursor.fetchone()

        if result:
            messagebox.showerror('Erro!', "Usuário já existe.")
        else:
            insert_user = 'INSERT INTO usuarios (usuario, senha) VALUES (%s, %s)'
            cursor.execute(insert_user, (user, passw))
            db.commit()
            messagebox.showinfo('Sucesso!', "Usuário cadastrado com sucesso.")
            tela_cadastro.destroy()
            abrir_tela_login()

    except mysql.connector.Error as err:
        messagebox.showerror('Erro!', f'Erro ao conectar ao banco de dados: {err}')

    finally:
        cursor.close()
        db.close()

def abrir_tela_cadastro():
    global usuario_entry, senha_entry, confirm_senha_entry, tela_cadastro
    root.destroy()

    tela_cadastro = Tk()
    tela_cadastro.geometry('400x500')
    tela_cadastro.title('Cadastro')
    tela_cadastro.config(bg='grey18')

    Label(tela_cadastro, text="Preencha os dados abaixo:", font=("Titan One", 18, "bold"), bg='grey18', fg='white').place(relx=0.5, rely=0.15, anchor="center")

    Label(tela_cadastro, text='Usuário', font=('Titan One', 15, "bold"), bg='grey18', fg='white').place(relx=0.5, rely=0.30, anchor="center")
    usuario_entry = Entry(tela_cadastro, font=('Titan One', 15, "bold"))
    usuario_entry.place(relx=0.5, rely=0.35, anchor="center")

    Label(tela_cadastro, text="Senha", font=("Titan One", 15, "bold"), bg='grey18', fg='white').place(relx=0.5, rely=0.45, anchor="center")
    senha_entry = Entry(tela_cadastro, font=("Titan One", 15), show="*")
    senha_entry.place(relx=0.5, rely=0.5, anchor="center") 

    Label(tela_cadastro, text="Confirmar Senha", font=("Titan One", 15, "bold"), bg='grey18', fg='white').place(relx=0.5, rely=0.6, anchor="center")
    confirm_senha_entry = Entry(tela_cadastro, font=("Titan One", 15), show="*")
    confirm_senha_entry.place(relx=0.5, rely=0.65, anchor="center") 

    style = ttk.Style()
    style.configure('custom.TButton', font=('Titan One', 12, "bold"), padding=(10.5), anchor="center") 

    btn_cadastrar = ttk.Button(tela_cadastro, text="Cadastrar", command=confirmar_cadastro, style='custom.TButton')
    btn_cadastrar.place(relx=0.5, rely=0.9, anchor="center")

def abrir_tela_login():
    global usuario_entry, senha_entry, root

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

    btn_cadastrar = ttk.Button(root, text="Cadastrar", command=abrir_tela_cadastro, style='custom.TButton')
    btn_cadastrar.place(relx=0.5, rely=0.9, anchor="center")

    root.mainloop()

if __name__ == "__main__":
    abrir_tela_login()