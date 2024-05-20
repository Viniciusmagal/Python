largura = float(input('largura da parede:'))
altura = float(input('altura da parede:'))
área =  largura * altura
print('sua parede tem dimensão de {}x{} e sua área é de {}m2'.format(largura, altura, área))
tinta = área/2
print('para pintar essa parede você precisará de {}l de'.format(tinta))

