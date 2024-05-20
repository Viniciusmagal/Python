número = int(input('Digite Um Número Inteiro:'))
print('''escolha uma das bases para conversão:
[ 1 ] converter para binário
[ 2 ] converter para Octal
[ 3 ] converter para hexadecimal''')
opção = int(input('sua opção: '))
if opção == 1:
    print('{} convertido para binário'.format(bin(número)[2:]))
elif opção == 2:
    print('{} convertido para octal'.format(oct(número)[2:]))
elif opção == 3:
    print('{} convertido para hexadecimal'.format(hex(número)[2:]))
else:
    print('você não selecionou nada, tente novamente')