#06 - Escreva um algoritmo que receba uma lista de números e retorne a lista ordenada de forma crescente (Bubble sort).

lista = []

i = 1
while i < 11:
    try:
        num1 = float(input(f'- {i}° número: '))
        lista.append(num1)
        i += 1

    except ValueError:
        print('Erro. Digite um número. \n')

lista.sort()
print(f'\nNúmeros digitados (em ordem): {lista}\n')