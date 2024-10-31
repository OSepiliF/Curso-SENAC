#03 - Escreva uma função que verifique se uma palavra ou frase é um palíndromo (pode ser lida da mesma maneira de trás para frente).

texto = input('\nDigite uma palavra: ')

texto = texto.lower().replace(' ','').replace(',','').replace('.','')
invert = texto[::-1]

if texto == invert:
    print(f'\nA palavra é um palíndromo. {texto} = {invert}\n')
    
else:
    print(f'\nA palavra não é um palíndormo. {texto} = {invert}\n')

