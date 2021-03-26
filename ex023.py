num = int(input('\033[7;32mDigite um numero de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
fim = {'final':'\033[m', 'inicio':'\033[7;32m'}
print('{}Unidade: {}{}'.format(fim['inicio'], u, fim['final']))
print('{}Dezena: {}{}'.format(fim['inicio'], d, fim['final']))
print('{}Centena: {}{}'.format(fim['inicio'], c, fim['final']))
print('{}Milhar: {}{}'.format(fim['inicio'], m, fim['final']))

# print('É preciso subtrair 1 do len pois ele começa a contar a partir do 1 e [] a partir do 0 -->len {} quando na '
#      'caixa[] o valor ocupado iria até {}'.format(len(numero), unidade))
