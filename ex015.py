diaAlug = int(input('\033[1;44mQuantos dias alugados? '))
KmRodado = float(input('Quantos Km rodados? '))
tot = (60 * diaAlug) + (0.15 * KmRodado)
print('O total a pagar é de R${:.2f}\033[m'.format(tot))
