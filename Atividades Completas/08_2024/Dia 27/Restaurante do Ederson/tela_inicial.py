from tkinter import *
from tkinter import messagebox, ttk

def abrir_pratos_entrada():
    pratos_entrada = Toplevel()
    pratos_entrada.title("Pratos de Entrada")
    pratos_entrada.geometry("1900x1200")

def abrir_pratos_principais():
    pratos_principais = Toplevel()
    pratos_principais.title("Pratos Principais")
    pratos_principais.geometry("1900x1200")

def abrir_bebidas_alcolicas():
    bebidas_alcolicas = Toplevel()
    bebidas_alcolicas.title("Bebidas Alcólicas")
    bebidas_alcolicas.geometry("1900x1200")

def abrir_bebidas():
    bebidas = Toplevel()
    bebidas.title("Bebidas")
    bebidas.geometry("1900x1200")

def abrir_sobremesas():
    sobremesas = Toplevel()
    sobremesas.title("Sobremesas")
    sobremesas.geometry("1900x1200")

def abrir_menu_do_chef():
    menu_do_chef = Toplevel()
    menu_do_chef.title("Menu do Chef")
    menu_do_chef.geometry("1900x1200")

def inicial_tela(usuario):
    root = Tk()
    root.geometry("1920x1200")
    root.title("Tela Inicial")

    #img = PhotoImage(file="").place(relx=0.5 , rely=0.1, anchor="center")


    Label(root, text=("Bem Vindo ao Restaurante do seu Ederson!"), font=("Arial", 20, "bold")).place(relx=0.5, rely=0.35, anchor="center")
    Label(root, text=(f"Olá {usuario}"), font=("Arial", 20, "bold")).place(relx=0.5, rely=0.4, anchor="center")

    style = ttk.Style()
    style.configure('custom.TButton', font=('Arial', 10), padding=15, width=20)

    btn_pratos_entrada = ttk.Button(root, text="Pratos de Entrada", style='custom.TButton', command=abrir_pratos_entrada)
    btn_pratos_entrada.place(relx=0.5, rely=0.48, anchor="center")

    btn_pratos_principais = ttk.Button(root, text="Pratos Principais", style='custom.TButton', command=abrir_pratos_principais)
    btn_pratos_principais.place(relx=0.5, rely=0.54, anchor="center")

    btn_bebidas_alcolicas = ttk.Button(root, text="Bebidas Alcólicas", style='custom.TButton', command=abrir_bebidas_alcolicas)
    btn_bebidas_alcolicas.place(relx=0.5, rely=0.60, anchor="center")

    btn_bebidas = ttk.Button(root, text="Bebidas", style='custom.TButton', command=abrir_bebidas)
    btn_bebidas.place(relx=0.5, rely=0.66, anchor="center")

    btn_sobremesas = ttk.Button(root, text="Sobremesas", style='custom.TButton', command=abrir_sobremesas)
    btn_sobremesas.place(relx=0.5, rely=0.72, anchor="center")

    btn_menu_do_chef = ttk.Button(root, text="Menu do Chef", style='custom.TButton', command=abrir_menu_do_chef)
    btn_menu_do_chef.place(relx=0.5, rely=0.78, anchor="center")

    root.mainloop()
