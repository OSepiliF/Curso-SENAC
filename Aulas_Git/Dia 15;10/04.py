#04 - Faça um programa que verifique se um número fornecido é primo.
while True:
    try:
        num1 = int(input('\nDigite um número: '))

        if num1 < 0:
            print('Digite um valor positivo!')
            continue

    except ValueError:
        print('Erro. Digite um número inteiro. ')
        continue

    if num1 % 2 == 0:
        print(f'\nO número {num1} não é primo.\n')

    else:
        print(f'\nO número {num1} é primo.\n')
        break