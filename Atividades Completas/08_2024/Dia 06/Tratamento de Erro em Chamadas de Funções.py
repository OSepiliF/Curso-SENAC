def tratamento(num2):
        try:
            num2 = float(num2)
            print("Real:",num2,"\n")
            
        except ValueError:
            print("\nValor Inválido! \n")
        
        except tratamento:
            pass

num1 = input("\nNum 1°: ")
tratamento(num1)
