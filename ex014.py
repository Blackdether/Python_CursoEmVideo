celsius = float(input('\033[35mInforme a temperatura em °C: '))
fah = 9 / 5 * celsius + 32
kel = celsius + 273.15
print('A temperatura de {:.1f}°C correnponde a {:.1f}°F e {}K!'.format(celsius, fah, kel))
