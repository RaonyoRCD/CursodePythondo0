idadeA = int(input("Digite a primeira idade aqui: "))
idadeB = int(input("Digite a outra idade aqui: "))

if idadeA < idadeB:
    idadeC=idadeA # A "idadeC" é uma outra variável que abacei de criar e será utilizada pelo código SE, E SEMONTE SE, a condição do IF for VERDADEIRA. Ela copia e mantém salva o mesmo valor que foi atribuido a variável "idadeA" que foi digitado pelo usuário.
    idadeA=idadeB # "idadeA" assume o mesmo valor da variável "idadeB" que também foi atribuido seu valor pelo usuário.
    idadeB=idadeC # "idadeB" passa a ter o mesmo valor da variável "idadeC", que tinha obtido o valor anterior de "idadeA"
    print("A maior idade digitada foi de:",idadeA,"anos, e a outra idade menor é de:" ,idadeB, "anos.")
else:
    print("A maior idade digitada foi de:",idadeA,"anos, e a outra idade menor é de:" ,idadeB, "anos.")