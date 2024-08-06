while True:
    try:
        num1 = input("\nDigite um Número: ")
        num1 = float(num1)
        print("Real:",num1,"\n")
        break

    except ValueError:
        print("\nValor Inválido! \n")