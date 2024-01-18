nome=input("Digite o seu nome: ")
idadeCliente=int(input("Digite a sua idade: "))
idadeEsposa=int(input("Digite a idade de seu(a) parceiro(a): "))
mediaIdade=(idadeCliente+idadeEsposa)/2
diferençaIdade=idadeCliente-idadeEsposa
print("O seu nome é",nome,"a sua idade é de",idadeCliente,"anos, a diferença de idade entre vocês é de",diferençaIdade, "e a média de idade entre vocês dois é de:",mediaIdade)