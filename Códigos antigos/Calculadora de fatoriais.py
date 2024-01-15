num = int(input('Digite aqui o número a ser fatorado: '))
fatorial = num
contador = 1
while (num - contador) > 1:
    fatorial = fatorial * (num - contador)
    contador += 1
print ('O fatorial do número {0} é {1}.'.format(num,fatorial))