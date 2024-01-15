print ('Quantos anos terei em 2021?')
ano = int(input('Qual é o ano de seu nascimento?'))
while ano <= 1900 or ano >= 2021:
   print ('Data de nascimento inválida, tente novamente.')
   ano = int(input('Qual é o ano de seu nascimento?'))
idade = 2021 - ano
print ('Neste ano, até dia 31/12/2021, você fará {} anos.'.format(idade))