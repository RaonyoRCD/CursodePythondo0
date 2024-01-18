# Além de saber a utilização do IF e do ELSE, também estou fazendo a correta identação, ali nas lihas dos dois PRINTS (Uso do TAB pro Python entender q a linha de baixo far parte da linha de cima).

idade = int (input("Digite aqui a sua idade: "))

if idade >= 18:
    print("Você já é maior de idade!")
elif idade <=0:
    print("Coloque uma idade válida.")
else:
    print("Você ainda é menor de idade!")