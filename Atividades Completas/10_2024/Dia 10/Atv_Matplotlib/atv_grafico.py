import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'Atividades Completas\\10_2024\\Dia 10\\Atv_Matplotlib\\imdb_top_1000.csv')

df['Gross'] = df['Gross'].str.replace(',', '').astype(float) 
top_receitas = df[['Gross', 'Series_Title']].nlargest(20, 'Gross')

while True:
    try:
        escolher = int(input('''  

=============================================================
                                         |     Gráfico      |
=============================================================   
| 1 | Ver a duração dos filmes.          |      Linha       |
| 2 | Ver os gêneros mais assistidos.    |      Pizza       |
| 3 | Filmes de maior receita.           |      Linha       |
| 4 | Filmes de maior receita.           | Barra Horizontal |
| 5 | Filmes de maior receita.           |  Barra Vertical  |
| 6 | Sair                                      -----
                             
Escolha uma opção: '''))
        
    except ValueError:  
        print("Opção inválida. Por favor, escolha uma opção válida. ")
        continue

    if escolher == 1:
        while True:
            try:
                duracao_filme = int(input('''
=======================================================
                                      |    Duração    |                                            
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
            duracao = duracao.str.replace(r'\D+', '', regex=True).astype(float)

            # Linha
            if duracao_filme == 1:
                filtro = (duracao > 50) & (duracao <= 90)
                numeros = duracao[filtro].head(30)

                for i, value in enumerate(numeros):
                    plt.text(i, value + 0.3, f' {str(int(value))} min', ha='center', fontsize=8) 

                plt.plot(titulo[filtro].head(30), duracao[filtro].head(30), marker='o', color='blue', markerfacecolor='red')
                plt.xticks(rotation=(-90), fontsize=6)
                plt.ylabel('Duração', fontsize=12)
                plt.xlabel('Título', fontsize=12)
                plt.title('Filmes com Duração entre 50 e 90 minutos', fontsize=14)
                plt.grid(True)
                plt.show()
                continue
            
            # Linha
            elif duracao_filme == 2:
                filtro = (duracao > 90) & (duracao <= 120)
                numeros = duracao[filtro].head(30)

                for i, value in enumerate(numeros):
                    plt.text(i, value + 0.3, f' {str(int(value))} min', ha='center', fontsize=8)

                plt.plot(titulo[filtro].head(30), duracao[filtro].head(30), marker='o', color='blue', markerfacecolor='red')
                plt.xticks(rotation=(-90), fontsize=6)
                plt.ylabel('Duração', fontsize=12)
                plt.xlabel('Título', fontsize=12)
                plt.title('Filmes com Duração entre 90 e 120 minutos', fontsize=14)
                plt.grid(True)
                plt.show()
                continue
            
            # Linha
            elif duracao_filme == 3:
                filtro = duracao > 120
                numeros = duracao[filtro].head(30)

                for i, value in enumerate(numeros):
                    plt.text(i, value + 0.3, f' {str(int(value))} min', ha='center', fontsize=8)

                plt.plot(titulo[filtro].head(30), duracao[filtro].head(30), marker='o', color='blue', markerfacecolor='red')
                plt.xticks(rotation=(-90), fontsize=6)
                plt.yticks(fontsize=6)
                plt.ylabel('Duração', fontsize=9)
                plt.xlabel('Título', fontsize=9)
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

    if escolher == 2:
        genero = df['Genre'].head(200)
        genero_lista = genero.str.get_dummies(sep=', ') 
        genero_soma = genero_lista.sum() 

        espaco = [0.05] * len(genero_soma)
        plt.pie(genero_soma, labels=genero_soma.index, explode=espaco, autopct="%.2f%%", pctdistance=0.77, textprops={'fontsize': 7}, rotatelabels=True,)
        plt.text(0, 0, 'Gêneros Mais Assistidos', ha='center', va='center', fontsize=14, fontweight='bold')
        plt.show()
        continue

    elif escolher == 3:
        plt.plot(top_receitas['Gross'], top_receitas['Series_Title'], marker='o', color='blue', markerfacecolor='red')

        for i, value in enumerate(top_receitas['Gross']):
            plt.text(value, i, f'  ${value:,.0f} bi', ha='left', va='center', fontsize=8)
        
        plt.ylabel('Título)', fontsize=10)
        plt.xlabel('Receita', fontsize=10)
        plt.yticks(fontsize=7)
        plt.xticks(fontsize=7)
        plt.title('Filmes de Maior Receita', fontsize=14)
        plt.grid(True)
        plt.show()
        continue

    elif escolher == 4:
        plt.bar(top_receitas['Series_Title'], top_receitas['Gross'])
        plt.ylabel('Título)', fontsize=10)
        plt.xlabel('Receita', fontsize=10)
        plt.yticks(fontsize=7)
        plt.xticks(rotation=90, fontsize=7)
        plt.title('Filmes de Maior Receita', fontsize=14)
        plt.grid(True)
        plt.show()
    
    elif escolher == 5:
        plt.barh(top_receitas['Series_Title'], top_receitas['Gross'])
        plt.ylabel('Título)', fontsize=10)
        plt.xlabel('Receita', fontsize=10)
        plt.yticks(fontsize=7)
        plt.xticks(rotation=90, fontsize=7)
        plt.title('Filmes de Maior Receita', fontsize=14)
        plt.grid(True)
        plt.show()

    elif escolher == 6:
        print('Saindo...                                                      . . .\n')
        break

    else:
        print('Escolha dentre as opções! ')
        continue