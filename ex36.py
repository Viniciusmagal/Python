casa = float(input('Valor da casa: R$'))
saláriocomprador = float(input('Salário Do Comprador: R$'))
anos = float(input('Quantos Anos de financiamentos: '))
prestação = casa / (anos * 12)
minimo = saláriocomprador * 30/100
print('Para pagar uma casa de R${:.2f} em {} anos '.format(casa, anos), end='')
print('a prestação será de R$ {:.2f}'.format(prestação))
if prestação <=minimo:
    print('empréstimo concedido')
else:
    print('empréstimo negado')
