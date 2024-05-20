print('Bem vindo as Lojas magal!')
valor = float(input('Insira o valor do produto que deseja adquirir: R$ '))
print('Escolha a condição de pagamento:')
print('(1)A vista no dinheiro ou cheque.(2)A vista no cartão.(3)Parcelado no cartão')
cond = int(input('Digite o número correspondente: '))

if cond == 1:
    print(f'O valor a ser pago pelo produto será de R${valor - (valor * 0.1):.2f}')
elif cond == 2:
    print(f'O valor a ser pago pelo produto é de R${valor - (valor * 0.05):.2f}')
elif cond == 3:
    print('Em quantas parcelas deseja realizar o pagamento?')
    parc = int(input('Digite o número de parcelas: '))
    if parc <= 2:
        print(f'O valor a ser pago pelo produto é de R${valor:.2f} sem juros.')
    elif parc >= 3:
        valor = valor + (valor * 0.2)
        print(f'O valor a ser pago pelo produto é de R${valor:.2f} com juros.\nA ser pago em {parc} vezes de '
              f'R${valor / parc}.')
else:
    print('Opção inválida de pagamento. Tente novamente.')
print('Obrigado por escolher as Lojas magal!')