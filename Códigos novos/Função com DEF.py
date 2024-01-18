# Este tipo de função serve para que eu não precise ficar toda hora reescrevendo o mesmo código para repetir algum serviço solicitado ao usuário ou qualquer outro tipo de serviço que precisa refazer mais de uma vez. Posso ver no fim deste código que eu mando ele repetir por 3 vezes a mesma função descrita acima dele.

def nome1 (): # Defini (DEF) a função de nome: "nome1". Uso desta função para que ele refaça todo o serviço.
    nome=input("Digite seu nome aqui: ") # Dados do usuário
    idade=int(input("Digite a sua idade aqui: ")) # Dados do usuário
    
    print("O seu nome é",nome,"\nVocê possui",idade, "anos de idade\n") # Frase para o usuário com os dados que ele inseriu

# Esta função descrita acima será repetida sem precisar reescreve-la toda novamente. Basta eu "chamar" o NOME que eu dei pra função que esta função rodará automaticamente na mesa quantidade de chamadas que eu quiser colocar. Como já mensionado, irei chamar ela 3 vezes neste meu exemplo.

nome1() # Vez 1
nome1() # Vez 2
nome1() # Vez 3 e fim

# Veja que ele rodou o mesmo código lá de cima por 3 vezes.