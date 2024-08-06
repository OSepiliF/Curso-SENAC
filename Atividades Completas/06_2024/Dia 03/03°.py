#03 -Existência de um Triângulo: Crie um programa que recebe os três lados de um triângulo e passa esses valores para uma função que verifica se esse triângulo existe ou não. 
# Para que um triângulo exista, cada lado deve ser maior que o módulo da subtração dos outros dois lados e menor que a soma dos outros dois lados.

def lados(lado1, lado2, altura):
    lado1 = float(input("\nDigite o 1° lado: "))
    lado2 = float(input("\nDigite o 2° lado: "))
    altura = float(input("\nDigite a altura: "))
    if lado1 > (lado2 - altura) and lado1 < (lado2+altura) and lado2 > (lado1-altura) and lado2 < (lado1+altura) and altura > (lado1-lado2) and altura < (lado1+lado2):
        print("\nÉ um triângulo!\n")
    else:
        print("\nNão é um triangulo! \n")
lados(1,2,3)