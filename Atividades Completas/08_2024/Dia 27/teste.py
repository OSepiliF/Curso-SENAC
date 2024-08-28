from tkinter import *
from tkinter import PhotoImage

root = Tk()
root.title("Galeria de Imagens - Rafael Montiel")
root.geometry('650x550')

def Pingu():
    global img, img_label
    img = PhotoImage(file=r"C:\\Users\\FilipeSimoes\\Documents\\GitHub\\Atividades-SENAC\\Atividades Completas\\08_2024\\Dia 27\\Imagens_Galeria\\Paisagem1.png")
    img_label = Label(root, image=img).place(x=300,y=125)

def Moyai():
    global img,img_label
    img = PhotoImage(file=r"C:\\Users\\FilipeSimoes\\Documents\\GitHub\\Atividades-SENAC\\Atividades Completas\\08_2024\\Dia 27\\Imagens_Galeria\\Paisagem2.png",)
    img_label = Label(root, image=img).place(x=300,y=125)

def nenhum():
    global img,img_label
    img = None
    img_label = None

def describe_print():
    print(f"{describe_entry.get()}")
    describe_text = Label(root,text=describe_entry.get())
    describe_text.place(x=50,y=190)

button1 = Button(root, fg="white", bg="Dark Blue", text=" Pingu ",command=Pingu)
button1.place(x=50,y=35)

button2 = Button(root, fg="white", bg="black", text=" Moyai ",command=Moyai)
button2.place(x=50,y=60)

texto_testado = Label(root, text='IMAGENS',font='Arial')
texto_testado.place(x=50,y=10)
describe_label = Label(root, text="Descrição:")
describe_label.pack()
describe_entry = Entry(root)
describe_entry.pack()
describe_label.place(x=50,y=110)
describe_entry.place(x=50,y=135)

button4 = Button(root, fg='black',bg='white', text='Nenhum', command=nenhum)
button4.place(x=50,y=85)

button3 = Button(root, fg='black', bg='white', text='Print Descrição', command=describe_print)
button3.place(x=50,y=160)

root.mainloop()