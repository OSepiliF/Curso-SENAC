from tkinter import *
from tkinter import PhotoImage

root = Tk()
root.title("Galeria de Imagens")
root.geometry("800x600")

def Imagem1():
    global img, img_label
    img = PhotoImage(file=r"C:\\Users\\FilipeSimoes\\Documents\\GitHub\\Atividades-SENAC\\Atividades Completas\\08_2024\\Dia 27\\Imagens_Galeria\\Paisagem1.png")
    img_label = Label(root, image=img).place(x=300,y=125)

def Imagem2():
    global img, img_label
    img = PhotoImage(file=r"C:\\Users\\FilipeSimoes\\Documents\\GitHub\\Atividades-SENAC\\Atividades Completas\\08_2024\\Dia 27\\Imagens_Galeria\\Paisagem2.png")
    img_label = Label(root, image=img).place(x=300,y=125)

def Imagem3():
    global img, img_label
    img = PhotoImage(file=r"C:\\Users\\FilipeSimoes\\Documents\\GitHub\\Atividades-SENAC\\Atividades Completas\\08_2024\\Dia 27\\Imagens_Galeria\\Paisagem3.png")
    img_label = Label(root, image=img).place(x=300,y=125)