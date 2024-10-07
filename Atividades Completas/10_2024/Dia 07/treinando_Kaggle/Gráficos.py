import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("C:\\Users\\FilipeSimoes\\Documents\\GitHub\\Atividades-SENAC\\Atividades Completas\\10_2024\Dia 07\\treinando_Kaggle\\all_seasons.csv")

altura = df.loc[0:11145, ['player_height']]
peso = df.loc[0:11145, ['player_weight']]

plt.title(u'NBA Players')
plt.ylabel(u'Altura')
plt.xlabel(u'peso')

# Limita o tamanho do gráfico
plt.axis((0,10,0,10))

while True:
    try:
        escolha = int(input('''
1 = Linha 
2 = Linha Curva
3 = Pontos
4 = Barras
5 = Pizza
6 = Sair
                        
R: '''))
    except ValueError as err:
        print('\nInválido! \n')
        break

    if escolha == 1:
        # ------------------ Linha ------------------
        plt.plot((1,2,3,4,5),(1,2,3,4,5),'r--')
        plt.show()
    
    elif escolha == 2:
        # ------------------ Linha curva ------------------
        x = np.linspace(1,8,num=100)
        z = [t**2 for t in x]
        plt.plot(x,z,'b') 
        plt.show()

    elif escolha == 3:
        # ------------------ Pontos ------------------
        plt.scatter((1,2,3,4,5),(1,2,3,4,5)) 
        plt.show()

    elif escolha == 4:
        # ------------------ Barras ------------------
        plt.bar((1,2,3,4,5),(1,2,3,4,5))
        plt.show() 

    elif escolha == 5:
        # ------------------ Pizza ------------------ 
        a1 = [10,20,30]
        explode=(0.1,0,0)
        labels = ['HB20','Gol','Fusca']
        plt.pie(a1,explode=explode,
        labels = labels, autopct="%.2f%%", shadow=True) 
        plt.show()
    
    elif escolha == 6:
        print('\nSaindo... \n')
        break
