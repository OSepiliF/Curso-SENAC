from tkinter import *
from tkinter import messagebox,ttk
from PIL import Image, ImageTk
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
        cadastro.destroy()
        abrir_inicial_tela(usuario)


cadastro = Tk()
cadastro.title("Cadastro")
cadastro.state("zoomed")
cadastro.configure(bg='#F3F3F3')
cadastro.overrideredirect(True)

#Plano de Fundo
img_bg = (r"Imagens_Restaurante\\Madeira.jpg")
bg_image = Image.open(img_bg)
screen_width = cadastro.winfo_screenwidth()
screen_height = cadastro.winfo_screenheight()
bg_image = bg_image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
bg_image_tk = ImageTk.PhotoImage(bg_image)
bg_label = Label(cadastro, image=bg_image_tk)
bg_label.place(relwidth=1, relheight=1)

#Barra de Titulo
barra_titulo = Frame(cadastro, bg='black', bd=2)
barra_titulo.pack(fill=X)
titulo_label = Label(barra_titulo, text="Restaurante do Ederson", font=("Titan One", 12, "bold"), bg='black', fg='white')
titulo_label.pack(side=LEFT, padx=10)
close_button = Button(barra_titulo, text=" X ", bg='black', fg='red', command=cadastro.destroy)
close_button.pack(side=RIGHT, padx=10)

quadrado = Frame(cadastro, bg='lightgray', width=600, height=770)
quadrado.place(relx=0.5, rely=0.47, anchor='center')

img = PhotoImage(file="Imagens_Restaurante\\Logo_Recortada.png")
Label(cadastro, image=img, bg='lightgray').place(relx=0.5, rely=0.25, anchor="center")

Label(cadastro, text=("Preencha os dados abaixo:"), font=("Titan One", 18, "bold"), bg='lightgray').place(relx=0.5, rely=0.39, anchor="center")

Label(cadastro, text=("Usuário"), font=("Titan One", 15, "bold"), bg='lightgray').place(relx=0.5, rely=0.45, anchor="center")
usuario = Entry(cadastro, font=("Titan One", 15))
usuario.place(relx=0.5, rely=0.48, anchor="center")

Label(cadastro, text=("Senha"), font=("Titan One", 15, "bold"), bg='lightgray').place(relx=0.5, rely=0.55, anchor="center")
senha = Entry(cadastro, font=("Titan One", 15), show="*")
senha.place(relx=0.5, rely=0.58, anchor="center")

Label(cadastro, text=("Confirmar Senha"), font=("Titan One", 15, "bold"), bg='lightgray').place(relx=0.5, rely=0.65, anchor="center")
confirmar_senha = Entry(cadastro, font=("Titan One", 15), show="*")
confirmar_senha.place(relx=0.5, rely=0.68, anchor="center")

style = ttk.Style()
style.configure('custom.TButton', font=('Titan One', 15, "bold"), bg='lightgray', padding=(10.5), anchor="center")
btn = ttk.Button(cadastro, text="Cadastrar", command=verificacao, style='custom.TButton')
btn.place(relx=0.5, rely=0.75, anchor="center")

cadastro.mainloop()