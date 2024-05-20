nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))
média = (nota1 + nota2) / 2
print('tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, média))
if média >= 5 and média < 7:
    print('o aluno está de recuperação')
elif média < 5:
    print('o aluno está reprovado')
elif média >= 7:
    print('o aluno está aprovado')