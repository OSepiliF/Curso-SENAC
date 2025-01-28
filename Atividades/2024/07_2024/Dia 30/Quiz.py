
while True:
    q_1 = str(input("Qual é a Capital do Brasil? ")).capitalize()
    if q_1 != 'Brasília':
        print("Resposta Incorreta. ")
        continue
    
    q_2 = int(input("Em que ano foi proclamado a Independência do Brasil? "))
    if q_2 != 1822:
        print("Resposta Incorreta. ")
        continue

    q_3 = int(input("Quantos estados compõem o Brasil? "))
    if q_3 != 27:
        print("Resposta Incorreta. ")
        continue

    q_4 = int(input("Qual é a raiz quadrada de 9? "))
    if q_4 != 3:
        print("Resposta Incorreta. ")
        continue

    print("""==----- Acertos -----==""")