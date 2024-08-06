estoque = []

while True:
    escolha = int(input("""                   
| 1 | Adicionar Produtos
| 2 | Remover Produtos
| 3 | Exibir Estoque
| 4 | Sair

Escolha: """))
    
    if escolha == 1:
        nome_produto = str(input("Digite o nome do produto: "))
        estoque.append(nome_produto)

    elif escolha == 2:
        print(estoque)
        remov_prod = str(input("Digite o nome do produto que deseja remover: "))
        estoque.remove(remov_prod)

    elif escolha == 3:
        print("\n=----- Estoque -----=")
        for item in estoque:
            print(f"- {item}")
        print("=-------------------=")

    elif escolha == 4:
        break

    else:
        print("Inválido! ")
        continue