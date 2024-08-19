from tkinter import *
from tkinter import ttk


n1 = 0
def botao(): #botao +
    global n1
    n1 += 1
    print('-',n1)
    

root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(frm, text="Clique no botão :D",font="ariel 20").grid(column=1, row=0)
ttk.Button(frm, text=f"Clicado: {n1}", command=botao).grid(column=1, row=1)
root.mainloop()