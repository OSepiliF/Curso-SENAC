import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np


df = pd.read_csv("C:\\Users\\FilipeSimoes\\Documents\\GitHub\\Atividades-SENAC\\Atividades Completas\\10_2024\Dia 07\\treinando_Kaggle\\all_seasons.csv")

salario = df.loc[0:200, ['player_height']]
ano = df.loc[0:200, ['player_weight']]


plt.title('Sálario Mínimo - NBA')
plt.ylabel(u'Válor')
plt.xlabel(u'Ano')
plt.bar(ano,salario)
plt.show()