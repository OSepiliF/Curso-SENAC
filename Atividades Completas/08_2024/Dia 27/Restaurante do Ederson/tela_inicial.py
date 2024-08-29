from tkinter import *
from tkinter import messagebox, ttk

def inicial_tela(usuario):
    root = Tk()
    root.geometry("1920x1200")
    root.title("Tela_Inicial")
    Label(root, text=(f"Bem Vindo! {usuario}"), font=("Arial", 20, "bold")).place(relx=0.532, rely=0.25, anchor="e")

    root.mainloop()