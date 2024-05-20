velocidade = float(input('qual é a velocidade atual do carro?'))
if velocidade > 80:
    print('multado, você passou do limite permitido de 80 km/h')
    multa = float (velocidade-80) * 7
print('você deve pagar uma multa de R${:.2f}'.format(multa))
print('tenha um bom dia, dirija com segurança'.format(velocidade < 80))