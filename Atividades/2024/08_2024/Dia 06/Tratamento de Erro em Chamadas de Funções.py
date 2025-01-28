while True:
    def tratamento(num2):
        try:
            num2 = float(num2)
            print("Real:",num2)
            
        except ValueError:
            print("\nValor Inválido! \n")

    num1 = input("\nDigite um número: ")
    tratamento(num1)
    break
