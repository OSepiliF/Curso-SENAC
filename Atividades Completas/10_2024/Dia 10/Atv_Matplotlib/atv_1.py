# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# df = pd.read_csv("C:\\Users\\FilipeSimoes\\Documents\\GitHub\\Atividades-SENAC\\Atividades Completas\\10_2024\\Dia 10\\Atv_Matplotlib\\imdb_top_1000.csv")



        
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("C:\\Users\\FilipeSimoes\\Documents\\GitHub\\Atividades-SENAC\\Atividades Completas\\10_2024\\Dia 10\\Atv_Matplotlib\\imdb_top_1000.csv")

# Extraindo os dados
titulo = df.loc[0:1000, ['Series_Title']]
# certificado = df.loc[0:1000, ['Certificate']]
duracao = df.loc[0:1000, ['Runtime']]
genero = df.loc[0:1000, ['Genre']]
avaliacao_imdb = df.loc[0:1000, ['IMDB_Rating']]
# descricao = df.loc[0:1000, ['Overview']]
# meta_score = df.loc[0:1000, ['Meta_score']]
# diretor = df.loc[0:1000, ['Director']]
# estrela1 = df.loc[0:1000, ['Star1']]
# estrela2 = df.loc[0:1000, ['Star2']]
# estrela3 = df.loc[0:1000, ['Star3']]
# estrela4 = df.loc[0:1000, ['Star4']]
# numero_votos = df.loc[0:1000, ['No_of_Votes']]
receita = df.loc[0:1000, ['Gross']]

while True:
    escolha_duracao = int(input('''
1 = Entre 30 min - 120 min


R:'''))

plt.bar(duracao, titulo)
plt.xticks(rotation=(-90), fontsize=6)  
plt.ylabel('Título', fontsize=12)
plt.xlabel('Duração (min)', fontsize=12)
plt.title('Duração dos Filmes', fontsize=14)
plt.show()




