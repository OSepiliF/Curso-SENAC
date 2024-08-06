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
    
    escreva ("Qual é o seu gênero: ")
    leia (sexo)

    escreva ("Escreva seu endereço: ")
    leia (endereco)

    escreva ("Digite seu número de telefone: ")
    leia (telefone)

    escreva ("\n\n<------------- Dados do Cliente -------------->\n\n")
    escreva("_________________________________\n")
    escreva("|Seu nome   |",nome,           "\n")
    escreva("|Sua idade  |",idade,          "\n")
    escreva("|Seu Gênero |",sexo,           "\n")
    escreva("|Endereço   |",endereco,      "\n")
    escreva("|Telefone   |",telefone,       "\n")
    escreva("_________________________________\n\n")

    cadeia nome
    real matem1, matem2, matem3, matem4
    real port1, port2, port3, port4
    real his1, his2, his3, his4
    real geo1, geo2, geo3, geo4
    real media1, media2, media3, media4
    cadeia escolha_nota
     
    escreva ("Você quer saber as médias do Aluno? (Sim) ou (Não) ")
    leia (escolha_nota)
    se (escolha_nota == "Sim"){

    escreva ("-> Notas escolares: \n\n")

    escreva ("\n\n -Sua nota do primeiro Bimestre \n")
    escreva (" Matematica: ")
    leia (matem1)
    escreva (" Português: ")
    leia (port1)
    escreva (" História: ")
    leia (his1)
    escreva (" Geografia: ")
    leia (geo1)

   escreva ("\n\n -Sua nota do Segundo Bimestre \n")
    escreva (" Matematica: ")
    leia (matem2)
    escreva (" Português: ")
    leia (port2)
    escreva (" História: ")
    leia (his2)
    escreva (" Geografia: ")
    leia (geo2)

    escreva ("\n\n -Sua nota do Terceiro Bimestre \n")
    escreva (" Matematica: ")
    leia (matem3)
    escreva (" Português: ")
    leia (port3)
    escreva (" História: ")
    leia (his3)
    escreva (" Geografia: ")
    leia (geo3)

    escreva ("\n\n -Sua nota do Quarto Bimestre \n")
    escreva (" Matematica: ")
    leia (matem4)
    escreva (" Português: ")
    leia (port4)
    escreva (" História: ")
    leia (his4)
    escreva (" Geografia: ")
    leia (geo4)

    escreva ("\n\n <---------- Notas de Cada Bimestre ----------> \n\n")
    escreva ("---Primeiro Bimestre--- \n\n")
    escreva (" Matematica: ",matem1, "\n")
    escreva (" Português: ",port1, "\n")
    escreva (" História: ",his1, "\n")
    escreva (" Geografia: ",geo1, "\n")

    escreva ("\n---Segundo Bimestre--- \n\n")
    escreva (" Matematica: ",matem2, "\n")
    escreva (" Português: ",port2, "\n")
    escreva (" História: ",his2, "\n")
    escreva (" Geografia: ",geo2, "\n")

    escreva ("\n---Terceiro Bimestre--- \n\n")
    escreva (" Matematica: ",matem3, "\n")
    escreva (" Português: ",port3, "\n")
    escreva (" História: ",his3, "\n")
    escreva (" Geografia: ",geo3, "\n")

    escreva ("\n---Quarto Bimestre--- \n\n")
    escreva (" Matematica: ",matem4, "\n")
    escreva (" Português: ",port4, "\n")
    escreva (" História: ",his4, "\n")
    escreva (" Geografia: ",geo4, "\n")

    media1 = (matem1 + matem2 + matem3 + matem4) / 2
    media2 = (port1 + port2 + port3 + port4) / 2
    media3 = (his1 + his2 + his3 + his4) / 2
    media4 = (geo1 + geo2 + geo3 + geo4) / 2

    escreva ("\n\n <---------- Médias das Diciplinas ----------> \n\n")
    escreva (" Matematica: ",media1, "\n")
    escreva (" Português: ",media2, "\n")
    escreva (" História: ",media3, "\n")
    escreva (" Geografia: ",media4, "\n")}
    senao {escreva ("Programa Encerrado. ")}
  }
}
