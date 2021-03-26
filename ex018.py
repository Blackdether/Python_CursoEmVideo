import math
angulo = float(input('\033[1;44mDigite o ângulo: '))
grausToRad = math.radians(angulo)
seno = math.sin(grausToRad)
cosseno = math.cos(grausToRad)
tangente = math.tan(grausToRad)
print('O ângulo {}°({:.2f} radianos) tem como seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(angulo, grausToRad, seno, cosseno, tangente))
