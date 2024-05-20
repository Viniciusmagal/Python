import _random
import random

aluno = str(input('digite o primeiro aluno: '))
aluno2 = str(input('digite o segundo aluno: '))
aluno3 = str(input('digite o terceiro aluno: '))
aluno4 = str(input('digite o quarto aluno: '))
lista = [aluno, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print('o aluno escolhido foi: {}'.format(escolhido))
