from tkinter import *
from tkinter import Tk, ttk

calculadora = Tk()
calculadora.title("Calculadora")
calculadora.geometry("400x400")

style = ttk.Style()
style.configure('custom.TButton', bg='red', font=('Arial',16), padding=4, width=4)

def printada(dados_em_casa):
    entrada = dados_em_casa.get()
    resultado = eval(entrada)
    dados_em_casa.delete(0, 'end')
    dados_em_casa.insert('end', resultado)
    print(resultado)

def botoes():
    global frame_buttons
    frame_buttons = Frame(calculadora, bg='gray18', width=400, height=400)
    frame_buttons.place(relx=0.5, rely=0.5, anchor='center')

    num_linhas = 4
    num_colunas = 5

    lista = ['>','1','2','3','÷','AC','4','5','6','x','√','7','8','9','-','%',',','0','=','+']

    largura_botao = 60  
    altura_botao = 40   

    for linha in range(num_linhas):
        for coluna in range(num_colunas):
            index = linha * num_colunas + coluna
            if index < len(lista):
                
                botao = ttk.Button(frame_buttons, style='custom.TButton', command=dados_em_casa.insert('end',), text=f"{lista[index]}")
                x = 30 + coluna * (largura_botao + 10)  
                y = 160 + linha * (altura_botao + 10)    
                botao.place(x=x, y=y, width=largura_botao, height=altura_botao) 
                print("x=",x,"/ y=",y, "/ Coluna=", coluna,"/ Linha=",linha)
botoes()

digite = Entry(frame_buttons, font=("Arial", 20), width=22).place(relx=0.5, rely=0.2, anchor='center')
marca = Label(frame_buttons, text="FELELP's", font=("Titan One", 12, "bold"), bg='gray18', fg='white').place(relx=0.18, rely=0.1, anchor='center')

calculadora.mainloop()