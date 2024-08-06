entrada = "1"
saida   = "Sair"
note  = 10
cell = 10
tab  = 10
fone  = 10
placa  = 10
mouse = 10

while entrada != saida:

    prod = input(f"""
VOUCHER DESENVOLVEDOR S.A

+=========================+-------------------
|  Código   |   Produto   |    Quantidade 
+===========+=============|-------------------
|    101    | -Notebook   |   {note}
|    202    | -Celular    |   {cell}
|    303    | -Tablet     |   {tab}
|    404    | -Fone       |   {fone}
|    505    | -Placa Mãe  |   {placa}
|    606    | -Mouse      |   {mouse}
+=========================+-------------------

Digite o Código do Produto que deseja Operar: """)

    while prod == "101":
        print("\n- NOTEBOOK SELECIONADO -")
        açao = input("""
+===============================+
|  Código  |      Operação      |
|----------+--------------------|
|     1    | Entrada do Estoque |
|----------+--------------------|
|     2    |  Saída de Estoque  |
|----------+--------------------|
|     3    |     Relatório      |
|----------+--------------------|
|     4    |       Sair         |
+===============================|

Digite o Código Da Operação: """)
        
        if açao == "1":
            op = int(input("\nQuantos Notebooks Seram Adicionados: "))
            note = op + note
            print("\nAdicionado ao estoque\n")

        elif açao == "2":
            op = int(input("\nQuantos Notebooks Seram Retirados: "))
            note = note - op 
            print("\nRetirado do Estoque\n")

        elif açao == "3":
            print(f"""
+=============+--------------------
|   Produto   |   Quantidade
|-------------|--------------------
| -Caderno    |   {note}
| -Celular    |   {cell}
| -Tablet     |   {tab}
| -Fone       |   {fone}
| -Placa Mãe  |   {placa}
| -Mouse      |   {mouse}
+=============+--------------------
""")
        elif açao == "4":
            if note < 0 and cell < 0 and tab < 0 and fone < 0 and placa < 0 and mouse < 0:
                print("\nQuantidade Invalida em Estoque\n")

            elif note >= 0 and cell >= 0 and tab >= 0 and fone >= 0 and placa >= 0 and mouse >= 0:
                break

        else:
            print("\nCódigo Invalido\n")

    while prod == "202":
        print("\n- CELULAR SELECIONADO -")
        açao = input("""
+===============================+
|  Código  |      Operação      |
|----------+--------------------|
|     1    | Entrada do Estoque |
|----------+--------------------|
|     2    |  Saída de Estoque  |
|----------+--------------------|
|     3    |     Relatório      |
|----------+--------------------|
|     4    |       Sair         |
+===============================|

Digite o Código Da Operação: """)
        
        if açao == "1":
            op = int(input("\nQuantos Celulares Seram Adicionados: "))
            cell = op + cell
            print("\nAdicionado ao estoque\n")

        elif açao == "2":
            op = int(input("\nQuantos Celulares Seram Retirados: "))
            cell = cell - op 
            print("\nRetirado do Estoque\n")

        elif açao == "3":
            print(f"""
+=============+-----------------
|   Produto   |   Quantidade
|-------------|-----------------
| -Caderno    |   {note}
| -Celular    |   {cell}
| -Tablet     |   {tab}
| -Fone       |   {fone}
| -Placa Mãe  |   {placa}
| -Mouse      |   {mouse}
+=============+-----------------
""")
        elif açao == "4":
            if note < 0 and cell < 0 and tab < 0 and fone < 0 and placa < 0 and mouse < 0:
                print("\nQuantidade Invalida em Estoque\n")

            elif note >= 0 and cell >= 0 and tab >= 0 and fone >= 0 and placa >= 0 and mouse >= 0:
                break

        else:
            print("\nCódigo Invalido\n")

    while prod == "303":
        print("\n- TABLET SELECIONADO -")
        açao = input("""
+===============================+
|  Código  |      Operação      |
|----------+--------------------|
|     1    | Entrada do Estoque |
|----------+--------------------|
|     2    |  Saída de Estoque  |
|----------+--------------------|
|     3    |     Relatório      |
|----------+--------------------|
|     4    |       Sair         |
+===============================|

Digite o Código Da Operação: """)
        
        if açao == "1":
            op = int(input("\nQuantos Tablet Seram Adicionados: "))
            tab = op + tab
            print("\nAdicionado ao estoque\n")

        elif açao == "2":
            op = int(input("\nQuantos Tablet Seram Retirados: "))
            tab = tab - op 
            print("\nRetirado do Estoque\n")

        elif açao == "3":
            print(f"""
+=============+-----------------
|   Produto   | Quantidade
|-------------|-----------------
| -Caderno    |   {note}
| -Celular    |   {cell}
| -Tablet     |   {tab}
| -Fone       |   {fone}
| -Placa Mãe  |   {placa}
| -Mouse      |   {mouse}
+=============+-----------------
""")
        elif açao == "4":
            if note < 0 and cell < 0 and tab < 0 and fone < 0 and placa < 0 and mouse < 0:
                print("\nQuantidade Invalida em Estoque\n")

            elif note >= 0 and cell >= 0 and tab >= 0 and fone >= 0 and placa >= 0 and mouse >= 0:
                break

        else:
            print("\nCódigo Invalido\n")

    while prod == "404":
        print("\n- FONE SELECIONADO -")
        açao = input("""
+===============================+
|  Código  |      Operação      |
|----------+--------------------|
|     1    | Entrada do Estoque |
|----------+--------------------|
|     2    |  Saída de Estoque  |
|----------+--------------------|
|     3    |     Relatório      |
|----------+--------------------|
|     4    |       Sair         |
+===============================|

Digite o Código Da Operação: """)
        
        if açao == "1":
            op = int(input("\nQuantos Fones Seram Adicionados: "))
            fone = op + fone
            print("\nAdicionado ao estoque\n")

        elif açao == "2":
            op = int(input("\nQuantos Fones Seram Retirados: "))
            fone = fone - op 
            print("\nRetirado do Estoque\n")

        elif açao == "3":
            print(f"""
+=============+-----------------
|   Produto   | Quantidade
|-------------|-----------------
| -Caderno    |   {note}
| -Celular    |   {cell}
| -Tablet     |   {tab}
| -Fone       |   {fone}
| -Placa Mãe  |   {placa}
| -Mouse      |   {mouse}
+=============+-----------------
""")
        elif açao == "4":
            if note < 0 and cell < 0 and tab < 0 and fone < 0 and placa < 0 and mouse < 0:
                print("\nQuantidade Invalida em Estoque\n")

            elif note >= 0 and cell >= 0 and tab >= 0 and fone >= 0 and placa >= 0 and mouse >= 0:
                break

        else:
            print("\nCódigo Invalido\n")

    while prod == "505":
        print("\n- PLACA MÃE SELECIONADO -")
        açao = input("""
+===============================+
|  Código  |      Operação      |
|----------+--------------------|
|     1    | Entrada do Estoque |
|----------+--------------------|
|     2    |  Saída de Estoque  |
|----------+--------------------|
|     3    |     Relatório      |
|----------+--------------------|
|     4    |       Sair         |
+===============================|

Digite o Código Da Operação: """)
        
        if açao == "1":
            op = int(input("\nQuantas Placas Mãe Seram Adicionadas: "))
            placa = op + placa
            print("\nAdicionado ao estoque\n")

        elif açao == "2":
            op = int(input("\nQuantas Placas Mãe Seram Retiradas: "))
            placa = placa - op 
            print("\nRetirado do Estoque\n")

        elif açao == "3":
            print(f"""
+=============+-----------------
|   Produto   | Quantidade
|-------------|-----------------
| -Caderno    |   {note}
| -Celular    |   {cell}
| -Tablet     |   {tab}
| -Fone       |   {fone}
| -Placa Mãe  |   {placa}
| -Mouse      |   {mouse}
+=============+-----------------
""")
        elif açao == "4":
            if note < 0 and cell < 0 and tab < 0 and fone < 0 and placa < 0 and mouse < 0:
                print("\nQuantidade Invalida em Estoque\n")

            elif note >= 0 and cell >= 0 and tab >= 0 and fone >= 0 and placa >= 0 and mouse >= 0:
                break

        else:
            print("\nCódigo Invalido\n")

    while prod == "606":
        print("\n- MOUSE SELECIONADO -")
        açao = input("""
+===============================+
|  Código  |      Operação      |
|----------+--------------------|
|     1    | Entrada do Estoque |
|----------+--------------------|
|     2    |  Saída de Estoque  |
|----------+--------------------|
|     3    |     Relatório      |
|----------+--------------------|
|     4    |       Sair         |
+===============================|

Digite o Código Da Operação: """)
        
        if açao == "1":
            op = int(input("\nQuantos Mouses Seram Adicionados: "))
            mouse = op + mouse
            print("\nAdicionado ao estoque\n")

        elif açao == "2":
            op = int(input("\nQuantos Mouses Seram Retirados: "))
            mouse = mouse - op 
            print("\nRetirado do Estoque\n")

        elif açao == "3":
            print(f"""
+=============+-----------------
|   Produto   | Quantidade
|-------------|-----------------
| -Caderno    |   {note}
| -Celular    |   {cell}
| -Tablet     |   {tab}
| -Fone       |   {fone}
| -Placa Mãe  |   {placa}
| -Mouse      |   {mouse}
+=============+-----------------
""")
        elif açao == "4":
            if note < 0 and cell < 0 and tab < 0 and fone < 0 and placa < 0 and mouse < 0:
                print("\nQuantidade Invalida em Estoque\n")

            elif note >= 0 and cell >= 0 and tab >= 0 and fone >= 0 and placa >= 0 and mouse >= 0:
                break

        else:
            print("\nCódigo Invalido\n")

    entrada = input("""
    Deseja Encerrar o Programa?
Aperte QUALQUER Tecla - Para CONTINUAR
Digite  "Sair"         - Para PARAR

- """).capitalize()

print(f"""
    VOUCHER DESENVOLVEDOR S.A

+===========+=============+-------------------
|  Código   |   Produto   |    Quantidade 
+===========+=============|-------------------
|    101    | -Caderno    |   {note}
|    202    | -Celular    |   {cell}
|    303    | -Tablet     |   {tab}
|    404    | -Fone       |   {fone}
|    505    | -Placa Mãe  |   {placa}
|    606    | -Mouse      |   {mouse}
+=========================+-------------------
""")