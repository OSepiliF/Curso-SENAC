#02 - Desenvolva um programa que mostre a tabuada de um número informado pelo usuário.

while True:
    try:
        num1 = int(input('\nDigite um número: '))
        mult = int(input('Até qual número deve ser multiplicado: '))

        if num1 < 0 or mult < 0:
            print('\nDigite um valor maior que 0! \n')
            continue

    except ValueError:
        print('\nErro. Digite um número inteiro.\n')
        continue

    cont = 0
    while cont < mult:
        cont += 1
        result = num1 * cont

        print(f'{num1}x{cont}: {result}')
    break

