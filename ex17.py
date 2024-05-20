from math import hypot
catetooposto = float(input('comprimento do cateto oposto: '))
catetoadjascente = float(input('comprimento do cateto adjascente: '))
hipotenusa = hypot(catetooposto, catetoadjascente)
print('a hipotenusa vai medir{:2f}'.format(hipotenusa))
