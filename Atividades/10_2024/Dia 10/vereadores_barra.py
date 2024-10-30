import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Frame, ttk

candidatos_vereador = [
    # Campo Grande
    {"nome": "Marquinhos Trad", "votos": 8567, "porcentagem": 1.95},  # 1
    {"nome": "Rafael Tavares", "votos": 8128, "porcentagem": 1.85},  # 2
    {"nome": "Carlão Comunitário Mesmo", "votos": 6912, "porcentagem": 1.57},  # 3
    {"nome": "Silvio Pitu", "votos": 6409, "porcentagem": 1.46},  # 4
    {"nome": "Veterinário Francisco", "votos": 6371, "porcentagem": 1.45},  # 5
    {"nome": "Fabio Rocha", "votos": 6314, "porcentagem": 1.44},  # 6
    {"nome": "Professor Riverton", "votos": 6271, "porcentagem": 1.43},  # 7
    {"nome": "Junior Coringa", "votos": 6131, "porcentagem": 1.39},  # 8
    {"nome": "Dr. Victor Rocha", "votos": 5355, "porcentagem": 1.22},  # 9
    {"nome": "Professor Juari", "votos": 5050, "porcentagem": 1.15},  # 10
    {"nome": "Flavio Cabo Almi", "votos": 5003, "porcentagem": 1.14},  # 11
    {"nome": "Luiza Ribeiro", "votos": 4982, "porcentagem": 1.13},  # 12
    {"nome": "André Salineiro Agente Federal", "votos": 4782, "porcentagem": 1.09},  # 13
    {"nome": "Papy", "votos": 4641, "porcentagem": 1.06},  # 14
    {"nome": "Ana Portela", "votos": 4577, "porcentagem": 1.04},  # 15
    {"nome": "Neto Santos", "votos": 4576, "porcentagem": 1.04},  # 16
    {"nome": "Maicon Nogueira", "votos": 4236, "porcentagem": 0.96},  # 17
    {"nome": "Delei Pinheiro", "votos": 4179, "porcentagem": 0.95},  # 18
    {"nome": "Wilson Lands", "votos": 4148, "porcentagem": 0.94},  # 19
    {"nome": "Herculano Borges", "votos": 4119, "porcentagem": 0.94},  # 20
    {"nome": "Beto Avelar", "votos": 4063, "porcentagem": 0.92},  # 21
    {"nome": "Dr Jamal", "votos": 4030, "porcentagem": 0.92},  # 22
    {"nome": "Landmark", "votos": 4022, "porcentagem": 0.91},  # 23
    {"nome": "Dr Sandro", "votos": 3922, "porcentagem": 0.89},  # 24
    {"nome": "Betinho", "votos": 3877, "porcentagem": 0.88},  # 25
    {"nome": "Clodoilson Pires", "votos": 3859, "porcentagem": 0.88},  # 26
    {"nome": "Jean Ferreira", "votos": 3768, "porcentagem": 0.86},  # 27
    {"nome": "Professor João Rocha", "votos": 3693, "porcentagem": 0.84},  # 28
    {"nome": "Valdir Gomes", "votos": 3648, "porcentagem": 0.83},  # 29
    {"nome": "Dr Lívio", "votos": 3636, "porcentagem": 0.83}  # 30
]

candidatos_prefeito = [
    # Campo Grande
    {"nome": "Adriane Lopes", "partido": "PP", "votos": 140913, "porcentagem": 31.67},
    {"nome": "Rose Modesto", "partido": "UNIÃO", "votos": 131525, "porcentagem": 29.56},
    {"nome": "Beto Pereira", "partido": "PSDB", "votos": 115516, "porcentagem": 25.96},

    # Dourados
    {"nome": "Marçal Filho", "partido": "PSDB", "votos": 60418, "porcentagem": 50.05},
    {"nome": "Alan Guedes", "partido": "PP", "votos": 34027, "porcentagem": 28.19},
    {"nome": "Tiago Botelho", "partido": "PT", "votos": 17845, "porcentagem": 14.78},

    # Três Lagoas
    {"nome": "Dr. Cassiano Maia", "partido": "PSDB", "votos": 38076, "porcentagem": 68.61},
    {"nome": "Dr. Ruy Costa", "partido": "DC", "votos": 16027, "porcentagem": 28.88},
    {"nome": "Professor Vitor", "partido": "PSTU", "votos": 1392, "porcentagem": 2.51},

    # Corumbá
    {"nome": "Dr. Gabriel", "partido": "PSB", "votos": 28394, "porcentagem": 56.74},
    {"nome": "Luiz Antonio Pardal", "partido": "PP", "votos": 10659, "porcentagem": 21.30},
    {"nome": "André Campos", "partido": "PL", "votos": 5944, "porcentagem": 11.88},

    # Ponta Porã
    {"nome": "Eduardo Campos", "partido": "PSDB", "votos": 26473, "porcentagem": 51.76},
    {"nome": "Pompilio Júnior", "partido": "PL", "votos": 15195, "porcentagem": 29.71},
    {"nome": "Carlos Bernardo", "partido": "PDT", "votos": 8168, "porcentagem": 15.97}
]

def abrir_vereadores():
    plt.clf()  
    votos_v = [candidatos['votos'] for candidatos in candidatos_vereador]
    nomes_v = [candidatos['nome'] for candidatos in candidatos_vereador]
    
    plt.xticks(rotation=90, fontsize=6)  
    plt.yticks(fontsize=12)
    plt.title('Candidatos a Vereador', fontsize=14)
    plt.bar(nomes_v, votos_v)
    plt.show()

def abrir_prefeitos():
    plt.clf()  
    votos_p = [candidatos['votos'] for candidatos in candidatos_prefeito]
    nomes_p = [candidatos['nome'] for candidatos in candidatos_prefeito]

    plt.xticks(rotation=90, fontsize=6)  
    plt.yticks(fontsize=12)
    plt.title('Candidatos a Prefeito', fontsize=14)
    plt.bar(nomes_p, votos_p)
    plt.show()

escolha = Tk()
escolha.title('Escolha')
escolha.geometry('200x200')
painel_bt = Frame(escolha, bg='gray18', width=200, height=200)
painel_bt.place(relx=0.5, rely=0.5, anchor='center')

bnt_v = ttk.Button(painel_bt, text='Vereadores', command=abrir_vereadores)
bnt_v.place(relx=0.5, rely=0.4, anchor="center")

bnt_p = ttk.Button(painel_bt, text='Prefeitos', command=abrir_prefeitos)
bnt_p.place(relx=0.5, rely=0.6, anchor="center")

escolha.mainloop()
