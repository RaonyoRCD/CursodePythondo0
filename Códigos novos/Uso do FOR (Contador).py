print("Desde 0 (começo padrão): ")
for a in range (20):
    print(a) 

# Uma vez que "a" é menor do que 20 (condição), o comando print é executado.
# Essa condição é adicionada com o comando RANGE.
# A variável "a" é incrementada em 1 (incremento padrão) e é testado se o valor de "a" ainda é menor do que 20.
# O processo se repete até que o valor de "a" fique maior ou igual a 20.
# Neste instante, o laço termina e o programa segue a execução das instruções do bloco de repetição.
 
print("")

print("Desde 5: ")
for a in range (5, 20,): # Posso começar desde onde eu quiser a contagem, basta acrescentar um número antes da vírgula e após esta mesma vírgula acrescentar até onde meu contador vai chegar. Ele ainda considera que o número máximo que coloquei não aparecerá pois por padrão ele começaria do 0. Por isso, ele chega só até o 19.
    print(a) 

print("")

print("Desde 5: ")
for a in range (5, 20, 3): # Idêntico ao de cima, só que desta vez eu quero que ele conte de 3 em 3 posições, por isso tem aquele 3 ali no final da condição.
    print(a) 

print("")

print("Ordem decrescente: ")
for a in range (20, 5, -1): # Posso colocar pra contar de trás pra frente. comecei com 20 que é onde o contador começa e coloquei o 5 pois é até onde eu quero q ele vá (ele conta até o 6 respeitando a mesma regra de começar do 0),  e aquele -1 indica que irá pulando de -1 em -1 casas (se fosse outro valor, ele pularia do valor que foi colocado).
    print(a)