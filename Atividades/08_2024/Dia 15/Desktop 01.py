from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=165)
root.geometry('400x400')
frm.grid()
ttk.Label(frm, text="Olá Mundo!").grid(column=1, row=1)
ttk.Button(frm, text="Sair", command=root.destroy).grid(column=1, row=0)
root.mainloop()