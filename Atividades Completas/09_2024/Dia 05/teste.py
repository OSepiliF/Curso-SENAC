from tkinter import *
from tkinter import Tk, ttk

calculadora = Tk()
calculadora.title("Calculadora")
calculadora.geometry("800x800")

style = ttk.Style()
style.configure('custom.TButton', bg='red', font=('Arial',16), padding=4, width=4)

def printada(botao_texto):
    entrada_atual = dados_em_casa.get()
    
    if botao_texto == '=':
        try:
            resultado = eval(entrada_atual)
            dados_em_casa.delete(0, 'end')
            dados_em_casa.insert('end', str(resultado))
        except Exception as e:
            dados_em_casa.delete(0, 'end')
            dados_em_casa.insert('end', 'Erro')
    elif botao_texto == 'AC':
        dados_em_casa.delete(0, 'end')
    else:
        dados_em_casa.insert('end', botao_texto)

def botoes():
    global frame_buttons
    global dados_em_casa

    calculadora = Tk()
    calculadora.title("Calculadora")

    # Create a text entry widget
    dados_em_casa = Entry(calculadora, width=20, font=('Arial', 24))
    dados_em_casa.place(relx=0.5, rely=0.3, anchor='center')

    frame_buttons = Frame(calculadora, bg='gray18', width=400, height=400)
    frame_buttons.place(relx=0.5, rely=0.6, anchor='center')

    num_linhas = 4
    num_colunas = 5

    lista = ['>','1','2','3','÷','AC','4','5','6','x','√','7','8','9','-','%',',','0','=','+']

    largura_botao = 60  
    altura_botao = 40   

    for linha in range(num_linhas):
        for coluna in range(num_colunas):
            index = linha * num_colunas + coluna
            if index < len(lista):
                botao_texto = lista[index]
                if botao_texto == '÷':
                    botao_texto = '/'
                elif botao_texto == 'x':
                    botao_texto = '*'
                elif botao_texto == '√':
                    botao_texto = '**0.5'  # Square root
                
                botao = ttk.Button(frame_buttons, text=f"{botao_texto}", command=lambda texto=botao_texto: printada(texto))
                x = 30 + coluna * (largura_botao + 10)  
                y = 160 + linha * (altura_botao + 10)    
                botao.place(x=x, y=y, width=largura_botao, height=altura_botao) 
                print("x=",x,"/ y=",y, "/ Coluna=", coluna,"/ Linha=",linha)

    calculadora.mainloop()

botoes()

digite = Entry(frame_buttons, font=("Arial", 20), width=22).place(relx=0.5, rely=0.2, anchor='center')
marca = Label(frame_buttons, text="FELELP's", font=("Titan One", 12, "bold"), bg='gray18', fg='white').place(relx=0.18, rely=0.1, anchor='center')

calculadora.mainloop()