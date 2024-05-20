número = int(input('digite um número qualquer: '))
resultado = número % 2
print('o resultado foi'.format(resultado))
if resultado == 0:
    print('o número {} é par'.format(número))
else:
    print('o número {} é ímpar'.format(número))