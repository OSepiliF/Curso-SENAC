#08 - Crie um algoritmo que receba 5 números e exiba o maior e o menor número informados. 

lista = []

i = 1
while i < 6:
    try:
        num1 = float(input(f'- {i}° número: '))
        lista.append(num1)
        i += 1

    except ValueError:
        print('Erro. Digite um número. \n')

print(f'\nMaior número: {max(lista)}\nMenor número: {min(lista)} \n')