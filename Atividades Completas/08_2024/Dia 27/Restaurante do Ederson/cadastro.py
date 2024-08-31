from tkinter import *
from tkinter import messagebox,ttk
from tela_inicial import abrir_inicial_tela

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
        abrir_inicial_tela(usuario)

root = Tk()
root.title("Cadastro")
root.state("zoomed")
root.configure(bg='#F3F3F3')

#Configuração da Barra de Titulo
root.overrideredirect(True)
barra_titulo = Frame(root, bg='black', bd=2)
barra_titulo.pack(fill=X)
titulo_label = Label(barra_titulo, text="Restaurante do Ederson", font=("Titan One", 12, "bold"), bg='black', fg='white')
titulo_label.pack(side=LEFT, padx=10)
close_button = Button(barra_titulo, text=" X ", bg='black', fg='red', command=root.destroy)
close_button.pack(side=RIGHT, padx=10)

#Criar Retângulos
canvas = Canvas(root, bg='#F3F3F3', highlightthickness=0)
canvas.pack(fill=BOTH, expand=True)
canvas.create_rectangle(650,100,1270,900, fill="lightgray", outline="")

#Logo
img = PhotoImage(file="Imagens_Restaurante\\Logo_Recortada.png")
Label(root, image=img, bg='lightgray').place(relx=0.5, rely=0.25, anchor="center")

Label(root, text=("Preencha os dados abaixo:"), font=("Titan One", 18, "bold"), bg='lightgray').place(relx=0.5, rely=0.39, anchor="center")

Label(root, text=("Usuário"), font=("Titan One", 15, "bold"), bg='lightgray').place(relx=0.5, rely=0.45, anchor="center")
usuario = Entry(root, font=("Titan One", 15))
usuario.place(relx=0.5, rely=0.48, anchor="center")

Label(root, text=("Senha"), font=("Titan One", 15, "bold"), bg='lightgray').place(relx=0.5, rely=0.55, anchor="center")
senha = Entry(root, font=("Titan One", 15), show="*")
senha.place(relx=0.5, rely=0.58, anchor="center")

Label(root, text=("Confirmar Senha"), font=("Titan One", 15, "bold"), bg='lightgray').place(relx=0.5, rely=0.65, anchor="center")
confirmar_senha = Entry(root, font=("Titan One", 15), show="*")
confirmar_senha.place(relx=0.5, rely=0.68, anchor="center")

style = ttk.Style()
style.configure('custom.TButton', font=('Titan One', 15, "bold"), bg='lightgray', padding=(10,5), anchor="center")
btn = ttk.Button(root, text="Cadastrar", command=verificacao, style='custom.TButton')
btn.place(relx=0.5, rely=0.75, anchor="center")

root.mainloop()