from datetime import date
sexo = print('''Qual o seu sexo?
[1] Masculino
[2] Feminino ''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('Preencha o formulário abaixo')
elif opcao == 2:
    print('Você não precisa se alistar.')
    exit()
else:
    print('Opção inválida.')
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda falta(m) {} ano(s) para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} ano(s).'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))