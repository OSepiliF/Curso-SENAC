from tkinter import *
from tkinter import Tk, ttk, messagebox


def verif():
    if usuario.get() == '' or senha.get() == '' or conf_senha.get() == '':
        messagebox.showerror('Erro','Preencha todas as opções.')
    elif senha.get() != conf_senha.get():
        messagebox.showerror("Erro!","Senhas não coincidem. ")
    elif senha.get() == usuario.get():
        messagebox.showerror("Erro!","Senha e usuário não podem ser iguais. ")
    else:
        messagebox.showinfo("Sucesso!", f"O usuário {usuario.get()} foi cadastrado. ")
        usuario = usuario.get()


root = Tk()
root.geometry('500x500')
root.title('Login')

Label(root, text=("Preencha os dados abaixo:"), font=("Titan One", 18, "bold"), bg='grey18', fg='white').place(relx=0.5, rely=0.15, anchor="center")

Label(root, text='Usuário', font=('Titan One', 15), bg='grey18', fg='white' ).place(relx=0.5, rely=0.25)
usuario = Entry(root, font=('Titan One', 15)).place(relx=0.5, rely=0.30)

Label(root, text=("Senha"), font=("Titan One", 15, "bold"), bg='grey18', fg='white').place(relx=0.5, rely=0.45, anchor="center")
senha = Entry(root, font=("Titan One", 15), show="*").place(relx=0.5, rely=0.5, anchor="center")

Label(root, text=("Confirmar Senha"), font=("Titan One", 15, "bold"), bg='grey18', fg='white').place(relx=0.5, rely=0.60, anchor="center")
conf_senha = Entry(root, font=("Titan One", 15), show="*").place(relx=0.5, rely=0.65, anchor="center")

style = ttk.Style()
style.configure('custom.TButton', font=('Titan One', 12, "bold"), padding=(10.5), anchor="center")
btn = ttk.Button(root, text="Cadastrar", command=verif, style='custom.TButton').place(relx=0.5, rely=0.8, anchor="center")

root.mainloop()
