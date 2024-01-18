arquivo=open('Texto Criado nas Funções.txt','w') # Se o arquivo já existe, ele siplesmente irá abrir e ir para a próxima linha do código, senão, vai criar um arquivo novo com o nome que foi dado entre as aspas. Aqui eu quis criar em formato de TXT, mas tabém dá pra criar em outros tipos de arquivo, como docx (word) e xlsx (excel). PORÉM, no momento em que escrevo isso, estes outros dois tipos de arquivos são criados mas NÃO ABREM nos seus respectivos programas. Ainda não sei como resolver.

arquivo.write('\nTestando o primeiro Write\n') # Primeira frase que escrevo dentro do arquivo novo. O \n me dá uma quebra de linha para que o próximo write que eu desejo colocar não fique grudado com este aqui.
arquivo.write('Este é o segundo write que escrevo\n\n') # Segundo write que eu coloco.
arquivo.write('*** Se eu quiser, eu posso deletar este arquivo e mandar este código cria-lo novamente ao executá-lo. ***\n\n') # Terceiro write que eu coloco.
arquivo.close # Fechamento do arquivo após tudo estar concluído.

# Após rodar este código, um arquivo na extensão escolhida (txt neste caso) será criado na pasta pai de onde este código está inserido. Ao rodas, nada aparecerá no terminal. Para que eu possa ver o terminal as informações que foram aqui inseridas, basta eu abrir o outro código "Função Read".

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