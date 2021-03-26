from math import hypot

catetoOpostoY = float(input('\033[1m\033[7mDigite o cateto oposto(eixoY): '))
catetoAdjacenteX = float(input('Digite o cateto adjacente(eixoX): '))
# hipotenusa = sqrt(catetoOpostoY ** 2 + catetoAdjacenteX ** 2)
hi = hypot(catetoOpostoY, catetoAdjacenteX)
print('A hipotenusa do triângulo retângulo é {:.2f}.\033[m'.format(hi))
