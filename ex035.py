from math import fabs
a = float(input('Digite o primeiro comprimento: '))
b = float(input('Digite o segundo comprimento: '))
c = float(input('Digite o terceiro comprimento: '))

cores = {'sem':'\033[m', 'azul':'\033[36;1m'}
# Outra forma de calcular:
# a < b + c and b < a + c and c < a + b
if (fabs(b - c) < a < b + c) or (fabs(a - c) < b < a + c) or (fabs(a - b) < c < a + b):
    print('{}É possível formar um triângulo{}'.format(cores['azul'], cores['sem']))
else:
    print('NÃO é possível formar um triângulo'.format(cores['azul'], cores['sem']))
