numero = int(input('Digite um número para saber sua tabuada de 1 - 10: '))
print('Tabuada do número: {}\n'.format(numero))
print('-'*12)
print('\033[36m1  x {:2} = {}\n2  x {:2} = {}\n3  x {:2} = {}\n4  x {:2} = {}\n5  x {:2} = {}\n6  x {:2} = {}\n7  x {:2} = {}\n8  x {:2} = {}\n9  x {:2} = {}\n10 x {:2} = {}'.format(numero,numero*1, numero, numero*2, numero, numero*3, numero, numero*4, numero, numero*5, numero, numero*6, numero, numero*7, numero,numero*8, numero, numero*9, numero, numero*10), end='\n------------')
