from tkinter import *
from tkinter import messagebox,ttk

def verificacao():
    if usuario.get() == "" or senha.get() == "" or confirmar_senha.get() == "":
        messagebox.showerror("Erro! Por favor preencha todas as opções. ")
    elif senha.get() != confirmar_senha.get():
        messagebox.showerror("Erro! Senhas não coincidem. ")
    elif senha.get() == usuario.get():
        messagebox.showerror("Erro! Senha e usuário não podem ser iguais. ")
    else:
        messagebox.showinfo(f"Sucesso! O usuário {usuario.get()} foi cadastrado. ")

root = Tk()
root.geometry("600x400")
root.title("Tela de Cadastro")

Label(root, text="Usuário:", font=("Arial", 10, "bold")).place(relx=0.39, rely=0.25, anchor="center")
usuario = Entry(root, width=30)
usuario.place(relx=0.5, rely=0.3, anchor="center")

Label(root, text="Senha:", font=("Arial", 10, "bold")).place(relx=0.38, rely=0.4, anchor="center")
senha = Entry(root, width=30, show="*")
senha.place(relx=0.5, rely=0.45, anchor="center")

Label(root, text="Confirmar Senha:", font=("Arial", 10, "bold")).place(relx=0.44, rely=0.55, anchor="center")
confirmar_senha = Entry(root, width=30, show="*")
confirmar_senha.place(relx=0.5, rely=0.6, anchor="center")

btn = ttk.Button(root, text="Cadastrar", command=verificacao, style='custom.TButton')
btn.place(relx=0.5, rely=0.77, anchor="center")

root.mainloop()