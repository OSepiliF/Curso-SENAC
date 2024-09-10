from tkinter import *
from tkinter import Tk, ttk, messagebox

def verif():
    if usuario.get() == '' or senha.get() == '':
        messagebox.showerror('Erro','Preencha todas as opções.')
    elif senha.get() == usuario.get():
        messagebox.showerror("Erro!","Senha e usuário não podem ser iguais. ")
    #elif usuario.get() != users_cadastrados(usuario) or senha.get() != users_cadastrados(usuario):
    #   messagebox.showerror('Aviso!','Não há usuários com essas informações ')
    else:
        messagebox.showinfo("Sucesso!", f"O usuário {usuario.get()} foi cadastrado. ")
        usuario = usuario.get()

def cadastros():
    users_cadastrados = {'Filipe': '321',
                         'João': '123',
                         'Roberto': 'XD',
                         'Rafael': 'joaozinho123',
                         'Enzo': 'FizoL'}

def abrir_tela_cadastro():
    global usuario, senha, btn
    root = Tk()
    root.geometry('400x400')
    root.title('Login')
    root.config(bg='grey18')

    Label(root, text=("Preencha os dados abaixo:"), font=("Titan One", 18, "bold"), bg='grey18', fg='white').place(relx=0.5, rely=0.15, anchor="center")

    Label(root, text='Usuário', font=('Titan One', 15, "bold"), bg='grey18', fg='white' ).place(relx=0.5, rely=0.33, anchor="center")
    usuario = Entry(root, font=('Titan One', 15, "bold")).place(relx=0.5, rely=0.4, anchor="center")

    Label(root, text=("Senha"), font=("Titan One", 15, "bold"), bg='grey18', fg='white').place(relx=0.5, rely=0.53, anchor="center")
    senha = Entry(root, font=("Titan One", 15), show="*").place(relx=0.5, rely=0.60, anchor="center")

    style = ttk.Style()
    style.configure('custom.TButton', font=('Titan One', 12, "bold"), padding=(10.5), anchor="center")
    btn = ttk.Button(root, text="Entrar", command=verif, style='custom.TButton').place(relx=0.5, rely=0.8, anchor="center")

    root.mainloop()

if __name__ == "__main__":
    abrir_tela_cadastro()