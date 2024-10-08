import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Users\\filip\\OneDrive\\Documentos\\GitHub\\Atividade-SENAC\\Atividades Completas\\10_2024\\Dia 10\\Atv_Matplotlib\\imdb_top_1000.csv')

while True:
    try:
        escolher = int(input('''  
=======================================================
                                       |     Menu     |   
| 1 | Ver a duração dos filmes 
| 2 | Ver os gêneros mais assistidos
| 3 | Ver os filmes de maior receita  
| 4 | Sair                  

Escolha uma opção: '''))
    except ValueError:  
        print("Opção inválida. Por favor, escolha uma opção válida. ")
        continue
    
    if escolher == 1:
        while True:
            try:
                duracao_filme = int(input('''
======================================================
                                       |   Duração   |                                            
| 1 | Entre 50 minutos a 90 minutos  
| 2 | Entre 90 minutos a 120 minutos
| 3 | Mais de 120 minutos  
| 4 | Voltar                  

Escolha uma opção: '''))
            except ValueError:
                print("Opção inválida. Por favor, escolha uma opção válida. ")
                continue

            titulo = df['Series_Title']
            duracao = df['Runtime']
            duracao = duracao.str.extract(r'(\d+)').astype(float).squeeze()  # Transformar em float

            if duracao_filme == 1:
                filtro = (duracao > 50) & (duracao <= 90)
                numeros = duracao[filtro].head(30)

                for i, value in enumerate(numeros):
                    plt.text(i, value + 0.5, f' {str(int(value))} min', ha='center', fontsize=8) # Colocar os números no marker

                plt.plot(titulo[filtro].head(30), duracao[filtro].head(30), marker='o', color='blue', markerfacecolor='red')
                plt.xticks(rotation=(-90), fontsize=6)
                plt.ylabel('Duração', fontsize=12)
                plt.xlabel('Título', fontsize=12)
                plt.title('Filmes com Duração entre 30 e 50 minutos', fontsize=14)
                plt.grid(True)
                plt.show()
                continue

            elif duracao_filme == 2:
                filtro = (duracao > 90) & (duracao <= 120)
                numeros = duracao[filtro].head(30)

                for i, value in enumerate(numeros):
                    plt.text(i, value + 0.5, f' {str(int(value))} min', ha='center', fontsize=8)

                plt.plot(titulo[filtro].head(30), duracao[filtro].head(30), marker='o', color='blue', markerfacecolor='red')
                plt.xticks(rotation=(-90), fontsize=6)
                plt.ylabel('Duração', fontsize=12)
                plt.xlabel('Título', fontsize=12)
                plt.title('Filmes com Duração entre 50 e 90 minutos', fontsize=14)
                plt.grid(True)
                plt.show()
                continue

            elif duracao_filme == 3:
                filtro = duracao > 120
                numeros = duracao[filtro].head(30)

                for i, value in enumerate(numeros):
                    plt.text(i, value + 0.5, f' {str(int(value))} min', ha='center', fontsize=8)

                plt.plot(titulo[filtro].head(30), duracao[filtro].head(30), marker='o', color='blue', markerfacecolor='red')
                plt.xticks(rotation=(-90), fontsize=6)
                plt.ylabel('Duração', fontsize=12)
                plt.xlabel('Título', fontsize=12)
                plt.title('Filmes com Duração acima de 120 minutos', fontsize=14)
                plt.grid(True)
                plt.show()
                continue

            elif duracao_filme == 4:
                print('Voltando...                                                      . . .')
                break

            else:
                print('Escolha dentre as opções! ')
                continue

    elif escolher == 2:
        genero = df['Genre'].head(200)
        genero_lista = genero.str.get_dummies(sep=', ') 
        genero_soma = genero_lista.sum() 

        espaco = [0.03] * len(genero_soma)
        plt.pie(genero_soma, labels=genero_soma.index, explode=espaco, autopct="%.2f%%", textprops={'fontsize': 10}, rotatelabels=True)
        plt.text(0, 0, 'Gêneros Mais Assistidos', ha='center', va='center', fontsize=14, fontweight='bold')
        plt.show()
        continue

    elif escolher == 3:
        df['Gross'] = df['Gross'].str.replace(',', '').astype(float) # Transformar em float
        top_receitas = df[['Gross', 'Series_Title']].nlargest(20, 'Gross') # Ordenar pela receita
        plt.plot(top_receitas['Gross'], top_receitas['Series_Title'], marker='o', color='blue', markerfacecolor='red')

        for i, value in enumerate(top_receitas['Gross']):
            plt.text(value, i, f'  ${value:,.0f} bi', va='center', ha='left', fontsize=8)
        
        plt.xticks(rotation=(-90), fontsize=6)
        plt.ylabel('Título)', fontsize=12)
        plt.xlabel('Receita', fontsize=12)
        plt.title('Filmes de Maior Receita', fontsize=14)
        plt.grid(True)
        plt.show()
        continue

    elif escolher == 4:
        print("Saindo...                                                      . . .\n")
        break

    else:
        print('Escolha dentre as opções! ')
        continue
