from datetime import date
atual = date.today().year
nascimento = int(input('Ano De Nascimento:'))
idade = atual - nascimento
print('o atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('classificação: Mirim')
elif idade <= 14:
    print('classificação Infantil')
elif idade <= 19:
    print('classificação junior')
elif idade <= 25:
    print('classificação senior')
else:
    print('classificação master')