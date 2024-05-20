from random import randint
from time import sleep
computador = randint(0, 5)#faz o computador sortear o número random
print('-=-' * 20)
print('vou pensar em um número entre 0 e 5. tente adivinhar')
print('-=-' * 20)
jogador = int(input('em que número pensei?'))#jogador tenta adivinhar
print('processando')
sleep(5)
if jogador == computador:
    print('parabéns você me venceu')
else:
    print('ganhei eu pensei no número {} e não no {}'.format(computador, jogador))