from tkinter import *
from tkinter import Tk, ttk

janela_calculadora = Tk()
janela_calculadora.title("Calculadora")
janela_calculadora.geometry("400x400")

estilo_bt = ttk.Style()
estilo_bt.configure('custom.TButton', bg='red', font=('Arial',16), padding=4, width=4)

def processar_bt(conteudo_bt):
    valor_atual = campo_entry.get()

    if conteudo_bt == '=':
        try:
            resultado = eval(valor_atual)
            campo_entry.delete(0, 'end')
            campo_entry.insert('end', str(resultado))
        except Exception as e:
            campo_entry.delete(0, 'end')
            campo_entry.insert('end', 'Erro')
    elif conteudo_bt == 'AC':
        campo_entry.delete(0, 'end')
    elif conteudo_bt == '⌫':
        campo_entry.delete(len(valor_atual) - 1, 'end')
    else:
        campo_entry.insert('end', conteudo_bt)

def criar_botoes():
    global painel_bt, campo_entry

    painel_bt = Frame(janela_calculadora, bg='gray18', width=400, height=400)
    painel_bt.place(relx=0.5, rely=0.5, anchor='center')

    campo_entry = Entry(painel_bt, font=("Arial", 20), width=22)
    campo_entry.place(relx=0.5, rely=0.2, anchor='center')

    rotulo_marca = Label(painel_bt, text="FELELP's", font=("Titan One", 12, "bold"), bg='gray18', fg='white')
    rotulo_marca.place(relx=0.18, rely=0.1, anchor='center')

    linhas_bt = 4
    colunas_bt = 5

    lista_bt = ['⌫','1','2','3','÷','AC','4','5','6','x','√','7','8','9','-','%',',','0','=','+']

    largura_botao = 60  
    altura_botao = 40   

    for linha in range(linhas_bt):
        for coluna in range(colunas_bt):
            index = linha * colunas_bt + coluna
            if index < len(lista_bt):
                conteudo_bt = lista_bt[index]
                if conteudo_bt == '÷':
                    conteudo_bt = '/'
                elif conteudo_bt == 'x':
                    conteudo_bt = '*'
                elif conteudo_bt == '√':
                    conteudo_bt = '**0.5'
                elif conteudo_bt == ',':
                    conteudo_bt = '.'

                botao = ttk.Button(painel_bt, style='custom.TButton', text=lista_bt[index], command= lambda texto=conteudo_bt: processar_bt(texto))
                x = 30 + coluna * (largura_botao + 10)  
                y = 160 + linha * (altura_botao + 10)    
                botao.place(x=x, y=y, width=largura_botao, height=altura_botao) 
                print("x=",x,"/ y=",y, "/ Coluna=", coluna,"/ Linha=",linha)

criar_botoes()
janela_calculadora.mainloop()