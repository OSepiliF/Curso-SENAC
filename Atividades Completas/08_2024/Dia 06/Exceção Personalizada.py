class Lulinha(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        print("\nFaz o L\n")

class Fez_o_L:
    while True:
        try:
            salario = float(input("\nQual é o seu salário? "))
            if salario <= 3000:
                raise Lulinha()
            elif salario > 3000:
                print("\nVocê será taxadd \n")
            break
            
        except ValueError:
            print("\nValor Inválido! \n")
        except Lulinha:
            pass