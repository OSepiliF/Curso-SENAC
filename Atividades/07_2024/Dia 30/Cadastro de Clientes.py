clientes = []

while True:
    
    nome = str(input("\nDigite o nome completo do cliente: ")).capitalize()
    rg = int(input("Digite o RG do cliente: "))
    cpf = int(input("Digite o CPF do cliente: "))
    telefone = int(input("Digite o telefone do cliente: "))
    clientes.append([nome,rg,cpf,telefone])

    sair = input("Digite (Sair) para sair: ").capitalize()

    if sair == "Sair":
        print(f"""\nCadastro de Saída: 
====================""")
        for cliente in clientes:
            print(f"Nome: {cliente[0]}, RG: {cliente[1]}, CPF: {cliente[2]}, Telefone: {cliente[3]}")
        break