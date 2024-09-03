from tkinter import *
from tkinter import messagebox, ttk, PhotoImage, Label
from PIL import Image, ImageTk

from carrinho import abrir_carrinho
from bebidas_alcoolicas import abrir_bebidas_alcoolicas
from bebidas import abrir_bebidas
from pratos_principais import abrir_pratos_principais
from menu_chef import abrir_menu_chef
from sobremesas import abrir_sobremesas
from pratos_entrada import abrir_pratos_entrada

def confirmar_sair():
    resposta = messagebox.askyesno("Confirmar Saída", "Você tem certeza que deseja sair?")
    if resposta:
        tela_inicial.destroy()

def abrir_inicial_tela(usuario):
    global tela_inicial
    tela_inicial = Tk()
    tela_inicial.title("Tela Inicial")
    tela_inicial.state("zoomed")
    tela_inicial.overrideredirect(True)

    #Plano de Fundo
    img_bg = (r"Imagens_Restaurante\\Madeira.jpg")
    bg_image = Image.open(img_bg)
    screen_width = tela_inicial.winfo_screenwidth()
    screen_height = tela_inicial.winfo_screenheight()
    bg_image = bg_image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
    bg_image_tk = ImageTk.PhotoImage(bg_image)
    bg_label = Label(tela_inicial, image=bg_image_tk)
    bg_label.place(relwidth=1, relheight=1)

    # Configuração da Barra de Título
    barra_titulo = Frame(tela_inicial, bg='black', bd=2)
    barra_titulo.pack(fill=X)
    titulo_label = Label(barra_titulo, text="Menu", font=("Titan One", 12, "bold"), bg='black', fg='white')
    titulo_label.pack(side=LEFT, padx=10)
    close_button = Button(barra_titulo, text=" X ", bg='black', fg='red', command=tela_inicial.destroy)
    close_button.pack(side=RIGHT, padx=10)

    quadrado = Frame(tela_inicial, bg='lightgray', width=750, height=940)
    quadrado.place(relx=0.5, rely=0.54, anchor='center')

    img = PhotoImage(file="Imagens_Restaurante\\Logo_Restaurante.png")
    Label(tela_inicial, image=img, bg='lightgray').place(relx=0.5, rely=0.35, anchor="center")

    Label(tela_inicial, text=("Seja Bem Vindo ao Nosso Restaurante!"), bg='lightgray', font=("Titan One", 20, "bold")).place(relx=0.5, rely=0.55, anchor="center")
    Label(tela_inicial, text=(f"Olá {usuario}"), bg='lightgray', font=("Titan One", 20, "bold")).place(relx=0.5, rely=0.6, anchor="center")

    style = ttk.Style()
    style.configure('custom.TButton', font=('Titan One', 12), bg='', padding=15, width=16)

    btn_pratos_entrada = ttk.Button(tela_inicial, text="Pratos de Entrada", style='custom.TButton', command=abrir_pratos_entrada)
    btn_pratos_entrada.place(relx=0.4, rely=0.7, anchor="center")

    btn_pratos_principais = ttk.Button(tela_inicial, text="Pratos Principais", style='custom.TButton', command=abrir_pratos_principais)
    btn_pratos_principais.place(relx=0.5, rely=0.7, anchor="center")

    btn_bebidas_alcoolicas = ttk.Button(tela_inicial, text="Bebidas Alcólicas", style='custom.TButton', command=abrir_bebidas_alcoolicas)
    btn_bebidas_alcoolicas.place(relx=0.6, rely=0.7, anchor="center")

    btn_bebidas = ttk.Button(tela_inicial, text="Bebidas", style='custom.TButton', command=abrir_bebidas)
    btn_bebidas.place(relx=0.4, rely=0.8, anchor="center")

    btn_sobremesas = ttk.Button(tela_inicial, text="Sobremesas", style='custom.TButton', command=abrir_sobremesas)
    btn_sobremesas.place(relx=0.5, rely=0.8, anchor="center")

    btn_menu_do_chef = ttk.Button(tela_inicial, text="Menu do Chef", style='custom.TButton', command=abrir_menu_chef)
    btn_menu_do_chef.place(relx=0.6, rely=0.8, anchor="center")

    bnt_carrinho = ttk.Button(tela_inicial, text="Carrinho", style='custom.TButton', command=abrir_carrinho)
    bnt_carrinho.place(relx=0.45, rely=0.9, anchor="center")

    bnt_sair = ttk.Button(tela_inicial, text="Sair", style='custom.TButton', command=confirmar_sair)
    bnt_sair.place(relx=0.55, rely=0.9, anchor="center")

    tela_inicial.mainloop()