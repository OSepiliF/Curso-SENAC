#02 - Hipotenusa de um Triângulo Retângulo: Crie um programa que recebe os dois lados menores de um triângulo retângulo e uma função retorna o valor da hipotenusa.

import math
def lados(lado1, lado2):
    lado1 = float(input("\nDigite o 1° lado: "))
    lado2 = float(input("\nDigite o 2° lado: "))
    print("\nHipotenusa:", math.sqrt(round(lado1**2 + lado2**2)),"\n")
lados(1,2)