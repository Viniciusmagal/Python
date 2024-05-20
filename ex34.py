salario = float(input('qual o salário do funcionário? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 /200)
print('quem ganhava R${:.2f} vai passar a ganhar {:.2f} agora'.format(salario, novo))