numero = int(input('Digite um número inteiro: '))
par = numero % 2
if par == 0 :
    print('\033[43mO número {} é PAR\033[m'.format(numero))
else:
    print('\033[45mO número {} é IMPAR\033[m'.format(numero))
