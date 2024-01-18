print("Laços até incrementar um valor correto:") # Aviso ao usuário
a = int(input("Digite aqui a sua idade: ")) # Condição
while a <=0: # Enquanto a for menor ou igual a 0
    print("Dados incorretos. Por favor, digite um número válido")
    a = int(input("Digite novamente a sua idade: ")) # Repetição da condição
b = int(input("Digite agora o seu ano de nascimento: "))# Condição
while b < 1900 or b >=2100: #Condições
    print("Ano incorreto. Por gentileza, digite um valor entre 1900 e 2099") # Aviso ao usuário
    b = int(input("Digite novamente o seu ano de nascimento: ")) # Repetição da condição

print("")

print("Agregando valor até o desejado:")
x=1
while x<= 5:
    print(x)
    x=x+1 # Incremento dentro do bloco de repetição
# É importante observar que, diferente da estrutura FOR, na estrutura WHILE temos de inicializar a variável antes do início do laço (x=1) e, também, realizar o incremento dentro do bloco de repetição (x=x+1).