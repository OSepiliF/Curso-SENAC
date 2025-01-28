lista = [0,1,2,3]

try:
    print(lista[0])
    print(lista[1])
    print(lista[2])
    print(lista[3])
    print(lista[4])
    
except IndexError:
    print("\nPosição Incorreta! \n")