programa {
  funcao inicio() {
    escreva ("       Senac HubAcademy\n\n")
  escreva ("-> Preencha seus dados logo abaixo: \n\n")

  cadeia nome
  inteiro idade 
  cadeia sexo
  cadeia endereco
  cadeia telefone

  escreva ("Digite o nome completo do aluno: ")
  leia (nome)
    

    escreva ("\nDigite sua idade: ")
    leia (idade)
    
    escreva ("Qual � o seu g�nero: ")
    leia (sexo)

    escreva ("Escreva seu endere�o: ")
    leia (endereco)

    escreva ("Digite seu n�mero de telefone: ")
    leia (telefone)

    escreva ("\n\n<------------- Dados do Cliente -------------->\n\n")
    escreva("_________________________________\n")
    escreva("|Seu nome   |",nome,           "\n")
    escreva("|Sua idade  |",idade,          "\n")
    escreva("|Seu G�nero |",sexo,           "\n")
    escreva("|Endere�o   |",endereco,      "\n")
    escreva("|Telefone   |",telefone,       "\n")
    escreva("_________________________________\n\n")

    cadeia nome
    real matem1, matem2, matem3, matem4
    real port1, port2, port3, port4
    real his1, his2, his3, his4
    real geo1, geo2, geo3, geo4
    real media1, media2, media3, media4
    cadeia escolha_nota
     
    escreva ("Voc� quer saber as m�dias do Aluno? (Sim) ou (N�o) ")
    leia (escolha_nota)
    se (escolha_nota == "Sim"){

    escreva ("-> Notas escolares: \n\n")

    escreva ("\n\n -Sua nota do primeiro Bimestre \n")
    escreva (" Matematica: ")
    leia (matem1)
    escreva (" Portugu�s: ")
    leia (port1)
    escreva (" Hist�ria: ")
    leia (his1)
    escreva (" Geografia: ")
    leia (geo1)

   escreva ("\n\n -Sua nota do Segundo Bimestre \n")
    escreva (" Matematica: ")
    leia (matem2)
    escreva (" Portugu�s: ")
    leia (port2)
    escreva (" Hist�ria: ")
    leia (his2)
    escreva (" Geografia: ")
    leia (geo2)

    escreva ("\n\n -Sua nota do Terceiro Bimestre \n")
    escreva (" Matematica: ")
    leia (matem3)
    escreva (" Portugu�s: ")
    leia (port3)
    escreva (" Hist�ria: ")
    leia (his3)
    escreva (" Geografia: ")
    leia (geo3)

    escreva ("\n\n -Sua nota do Quarto Bimestre \n")
    escreva (" Matematica: ")
    leia (matem4)
    escreva (" Portugu�s: ")
    leia (port4)
    escreva (" Hist�ria: ")
    leia (his4)
    escreva (" Geografia: ")
    leia (geo4)

    escreva ("\n\n <---------- Notas de Cada Bimestre ----------> \n\n")
    escreva ("---Primeiro Bimestre--- \n\n")
    escreva (" Matematica: ",matem1, "\n")
    escreva (" Portugu�s: ",port1, "\n")
    escreva (" Hist�ria: ",his1, "\n")
    escreva (" Geografia: ",geo1, "\n")

    escreva ("\n---Segundo Bimestre--- \n\n")
    escreva (" Matematica: ",matem2, "\n")
    escreva (" Portugu�s: ",port2, "\n")
    escreva (" Hist�ria: ",his2, "\n")
    escreva (" Geografia: ",geo2, "\n")

    escreva ("\n---Terceiro Bimestre--- \n\n")
    escreva (" Matematica: ",matem3, "\n")
    escreva (" Portugu�s: ",port3, "\n")
    escreva (" Hist�ria: ",his3, "\n")
    escreva (" Geografia: ",geo3, "\n")

    escreva ("\n---Quarto Bimestre--- \n\n")
    escreva (" Matematica: ",matem4, "\n")
    escreva (" Portugu�s: ",port4, "\n")
    escreva (" Hist�ria: ",his4, "\n")
    escreva (" Geografia: ",geo4, "\n")

    media1 = (matem1 + matem2 + matem3 + matem4) / 2
    media2 = (port1 + port2 + port3 + port4) / 2
    media3 = (his1 + his2 + his3 + his4) / 2
    media4 = (geo1 + geo2 + geo3 + geo4) / 2

    escreva ("\n\n <---------- M�dias das Diciplinas ----------> \n\n")
    escreva (" Matematica: ",media1, "\n")
    escreva (" Portugu�s: ",media2, "\n")
    escreva (" Hist�ria: ",media3, "\n")
    escreva (" Geografia: ",media4, "\n")}
    senao {escreva ("Programa Encerrado. ")}
  }
}
