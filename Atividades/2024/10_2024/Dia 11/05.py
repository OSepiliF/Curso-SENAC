#05  - Desenvolva uma função que mostre os n primeiros termos da sequência de Fibonacci, onde n é informado pelo usuário.

while True:
    try:
        num1 = int(input("\nDigite quantos termos você deseja: "))
        a = 0
        b = 1

        if num1 < 0:
            print('Digite um número maior que 0! ')
            continue

    except ValueError:
        print('Erro. Digite um número inteiro.')
        continue
    
    i= 0
    while i < num1:
        i += 1
        print(a, end=',')
        a, b = b, a + b
    print('[...]\n')
    break
