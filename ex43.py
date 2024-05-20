peso = float (input('qual o seu peso? (kg)'))
altura = float (input('qual é a sua altura? (m)'))
imc = peso / (altura ** 2)
print('o imc dessa pessoa é {:.1f}'.format(imc))
if imc < 18.5:
    print('você está abaixo do peso normal')
elif 18.5 <= imc < 25:
    print('parabéns, você está na faixa de peso normal')
elif 25 <= imc < 30:
    print('você está em sobrepeso')
elif 30 <= imc < 40:
    print('você está em obesidade, cuidado')
elif imc >= 40:
    print('você está em obesidade mórbida, cuidado')