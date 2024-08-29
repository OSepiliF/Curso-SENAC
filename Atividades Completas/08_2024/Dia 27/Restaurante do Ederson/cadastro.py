from tkinter import *
from tkinter import messagebox,ttk
from tela_inicial import inicial_tela

def verificacao():
    global usuario
    if usuario.get() == "" or senha.get() == "" or confirmar_senha.get() == "":
        messagebox.showerror("Erro!","Por favor preencha todas as opções. ")
    elif senha.get() != confirmar_senha.get():
        messagebox.showerror("Erro!","Senhas não coincidem. ")
    elif senha.get() == usuario.get():
        messagebox.showerror("Erro!","Senha e usuário não podem ser iguais. ")
    else:
        messagebox.showinfo("Sucesso!", f"O usuário {usuario.get()} foi cadastrado. ")
        usuario = usuario.get()
        root.destroy()
        inicial_tela(usuario)

root = Tk()
root.geometry("1920x1080")
root.title("Cadastro")
root.state("zoomed")

Label(root, text=("Preencha os dados abaixo!"), font=("Arial", 20, "bold")).place(relx=0.5, rely=0.2, anchor="center")

Label(root, text=("Usuário"), font=("Arial", 15, "bold")).place(relx=0.5, rely=0.37, anchor="center")
usuario = Entry(root, font=("Arial", 15))
usuario.place(relx=0.5, rely=0.4, anchor="center")

Label(root, text=("Senha"), font=("Arial", 15, "bold")).place(relx=0.5, rely=0.47, anchor="center")
senha = Entry(root, font=("Arial", 15), show="*")
senha.place(relx=0.5, rely=0.5, anchor="center")

Label(root, text=("Confirmar Senha"), font=("Arial", 15, "bold")).place(relx=0.5, rely=0.57, anchor="center")
confirmar_senha = Entry(root, font=("Arial", 15), show="*")
confirmar_senha.place(relx=0.5, rely=0.6, anchor="center")

style = ttk.Style()
style.configure('custom.TButton', font=('Arial', 15), padding=(10,5), anchor="center")
btn = ttk.Button(root, text="Cadastrar", command=verificacao, style='custom.TButton')
btn.place(relx=0.5, rely=0.7, anchor="center")

root.mainloop()