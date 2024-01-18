# Dando continuidade no código "Funções Open, Write e Close.py", lá eu criei um arquivo de texto e inseri dados dentro dele. Aqui neste código irei fazer a leitura do que foi criado.

leitura=open('Texto Criado nas Funções.txt','r') # Crio uma varável (leitura neste meu exemplo) e mado abrir o texto existente. O 'r' descreve que este arquivo é apara apenas LEITURA.
print(leitura.read()) # Printa na tela do usuário as informações contidas dentro do documento.
leitura.close() # Fechamento da função read.

# Aparecerá neste terminal as informações contidas no documento.

# *** Outros modos de leitura de arquivos: ***

# r	Abre o arquivo somente para leitura.
# O arquivo deve já existir.
# r+	Abre o arquivo para leitura e escrita. O arquivo deve já existir.
# A escrita começa a partir da primeira linha e, caso exista algo escrito no arquivo, as linhas serão reescritas, conforme formos escrevendo.
# w	Abre o arquivo somente para escrita, no início do arquivo.
# Apagará o conteúdo do arquivo se ele já existir. Criará um arquivo novo se não existir.
# w+	Abre o arquivo para escrita e leitura, apagando o conteúdo preexistente.
# a	Abre o arquivo para escrita no final do arquivo.
# Não apaga o conteúdo preexistente.
# a+	Abre o arquivo para escrita no final do arquivo e leitura.