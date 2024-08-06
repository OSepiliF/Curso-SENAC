#04 -Quadrado de Hashtags: Faça um programa que peça um número inteiro positivo ‘n’ ao usuário e imprima um quadrado de lado ‘n’ preenchido com hashtags. 
# Por exemplo, para n=4, o resultado seria:

####
####
####
####

def hashtags(n):
    n = int(input("\nDigite um número: "))
    for i in range(n):
        print("#"*n)
hashtags(1)