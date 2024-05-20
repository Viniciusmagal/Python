from math import radians, cos, tan, sin
angulo = float (input('digite o ângulo que você deseja:'))
seno = sin(radians(angulo))
print('o ângulo de {} tem o Seno de {2:f}'.format(angulo, seno))
cosseno =  cos(radians(angulo))
print('o ângulo de {} tem o cosseno {2:f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('o ângulo de {} tem a tangente de {:.2f}'.format(angulo, tangente))