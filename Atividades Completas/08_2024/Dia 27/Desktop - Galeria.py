from tkinter import *
import tkinter as tk
from tkinter import PhotoImage

root = Tk()
root.title("Galeria de Imagens")
root.geometry("1100x600")

def Imagem1():
    global img, img_label
    img = PhotoImage(file="C:\\Users\\FilipeSimoes\\Documents\\GitHub\\Atividades-SENAC\\Atividades Completas\\08_2024\\Dia 27\\Imagens_Galeria\\Paisagem1.png")
    img_label = Label(root, image=img).place(x=300,y=50)

def Imagem2():
    global img, img_label
    img = PhotoImage(file="C:\\Users\\FilipeSimoes\\Documents\\GitHub\\Atividades-SENAC\\Atividades Completas\\08_2024\\Dia 27\\Imagens_Galeria\\Paisagem2.png")
    img_label = Label(root, image=img).place(x=300,y=50)

def Imagem3():
    global img, img_label
    img = PhotoImage(file="C:\\Users\\FilipeSimoes\\Documents\\GitHub\\Atividades-SENAC\\Atividades Completas\\08_2024\\Dia 27\\Imagens_Galeria\\Paisagem3.png")
    img_label = Label(root, image=img).place(x=300,y=50)

def Nada():
    global img,img_label
    img = None
    img_label = None

def descricao_print():
    print(f"{descricao_entry.get()}")

botao1 = Button(root,fg='white', bg='Dark Blue', text='Imagem 1',command=Imagem1)
botao1.place(x=50,y=60)

botao2 = Button(root, fg='white', bg='Dark Blue', text='Imagem 2',command=Imagem2)
botao2.place(x=50,y=90)

botao3 = Button(root, fg='white', bg='Dark Blue', text='Imagem 3',command=Imagem3)
botao3.place(x=50,y=120)

texto = Label(root, text='IMAGENS',font='Arial')
texto.place(x=50, y=10)

descricao_label = Label(root,text='Descrição:')
descricao_label.pack()
descricao_label.place(x=50,y=210)

descricao_entry = Entry(root)
descricao_entry.pack()
descricao_entry.place(x=50, y=230)

botao4 = Button(root, fg='Black', bg='White',text='Nenhum', command=Nada)
botao4.place(x=50,y=150)

botao5 = Button(root, fg='Black', bg='White',text='Print', command=descricao_print)
botao5.place(x=50,y=260)

root.mainloop()