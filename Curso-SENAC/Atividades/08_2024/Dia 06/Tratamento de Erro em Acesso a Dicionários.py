dicionario = {
    'Olá':'\n-Bom Dia!\n',
    'Tchal':'\n-Adeus\n',
}
while True:
    try:
        chave = input("\nDigite a chave: ")
        print(dicionario[chave])
        break

    except KeyError:
        print("\nEssa chave não existe! ")