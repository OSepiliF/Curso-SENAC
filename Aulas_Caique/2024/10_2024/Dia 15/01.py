1 #01 - Crie uma função que calcule o fatorial de um número dado pelo usuário.

while True:
    try:
        num1 = int(input("\nDigite um número: "))

    except ValueError:
        print('Erro. Digite um número inteiro. ')
        continue

    result = 1
    for i in range(1, num1 + 1):
        result *= i
    
    print(f'\nO fatorial de {num1} é {result}\n')
    break