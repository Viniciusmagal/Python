distância = float (input('qual é a distância da viagem?'))
print('você está prestes a começar uma viagem de {}km'.format(distância))
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('e o preço de sua viagem será de R${:.2f}'.format(preço))