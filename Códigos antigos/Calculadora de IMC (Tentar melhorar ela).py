peso = float(input('Digite aqui o seu peso: '))
altura = float(input('Digite aqui a sua altura: '))
IMC = peso / (altura * altura)
if IMC <= 18.4:
    print ('o seu IMC é de {:.1f}, e você está abaixo do peso. Procure um especialista!'.format(IMC))
elif IMC >= 18.5 and IMC <= 24.9:
    print ('O seu IMC é de {:.1f}, e você está em um excelente peso! Continue assim!'.format(IMC))
elif IMC >= 25 and IMC <= 29.9:
    print('O seu IMC é de {:.1f}, e você está na categoria sobrepeso. Vá com calma! Faça dieta. Pratique exercícios!'.format(IMC))
elif IMC >= 30 and IMC <= 34.9:
    print('O seu IMC é de {:.1f}, e você está na obesidade de grau 1. Você precisa emagrecer. Procure um especialista!'.format(IMC))
elif IMC >= 35 and IMC <= 39.9:
    print('O seu IMC é de {:.1f}, e você está na obesidade de grau 2. Você precisa emagrecer. Procure um especialista!'.format(IMC))
else:
    print('O seu IMC é de {:.1f}, e você está na obesidade de grau 3. Você precisa emagrecer. Procure um especialista Urgente!'.format(IMC))