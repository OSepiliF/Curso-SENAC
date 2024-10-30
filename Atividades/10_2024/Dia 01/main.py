from usuario import Usuario

user = Usuario('banco_dados.db')

while True:
    print('''
| 1 | Criar Usuário
| 2 | Listar Usuário
| 3 | Atualizar Usuário
| 4 | Deletar Usuário
| 5 | Sair
''')
    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        nome = input('Nome: ')
        email = input('Email: ')
        user.CriarUser(nome, email)
        print('Usuário criado com sucesso! ')

    elif escolha == 2:
        usuarios = user.ListarUser()
        for i in usuarios:
            print(f'Nome: {i[1]} Email: {i[2]}')
    
    elif escolha == 3:
        id = int(input('ID: '))
        novo_nome = input('Novo Nome (deixe em branco para não alterar): ')
        novo_email = input('Novo Email (deixe em branco para não alterar): ')
        user.AtualizarUser(id, novo_nome or None, novo_email or None)
        print('Usuário atualizado com sucesso!')

    elif escolha == 4:
            id = int(input('ID do usuário a ser deletado: '))
            confirmacao = input('Tem certeza que deseja deletar este usuário? (s/n): ')
            if confirmacao.lower() == 's':
                user.DeletUser(id)
                print('Usuário deletado com sucesso!')
            else:
                print('Ação cancelada.')

    elif escolha == 5:
        print('Saindo...')
        break