#07 - Faça um programa que converta uma temperatura de Celsius para Fahrenheit e vice-versa. O usuário deverá escolher a conversão desejada.

while True:
    try:
        temp_C = float(input("\nDigite a temperatura desejada: "))
        temp_F = float ((9 * temp_C) / 5) + 32

    except ValueError:
        print('Erro. Digite um número.')
        continue

    print(f'\nC°: {temp_C}\nF°: {temp_F}\n')
    break