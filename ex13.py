salário = float(input('qual é o salário R$'))
novo = salário + (salário * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento passa a ganhar R${:.2f}'.format(salário, novo))
