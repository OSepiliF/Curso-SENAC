try:
    num1 = int(input("\nDigite o 1° número: "))
    num2 = int(input("Digite 2° número: "))

    num3 = num1/num2
    print(f"\nResultado: {num3}\n")

except ArithmeticError:
    print("Impossivel realizar a divisão por Zero! \n")

except ValueError:
    print("\nValor Inválido! \n")