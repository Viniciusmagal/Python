from random import shuffle
aluno = str(input('digite o primeiro aluno: '))
aluno2 = str(input('digite o segundo aluno: '))
aluno3 = str(input('digite o terceiro aluno: '))
aluno4 = str(input('digite o quarto aluno: '))
aluno5 = str(input('digite o quinto aluno: '))
lista = [aluno, aluno2, aluno3, aluno4, aluno5]
shuffle(lista)
print('a ordem será: ')
print(lista)