velocidade = float(input('Digite a velocidade do carro: '))
print('A velocidade do carro foi de {:.1f}Km/h'.format(velocidade))
if velocidade > 80 :
    print('Você ultrapassou o limite de velocidade e pagará uma {}multa de R${:.2f}{}'.format('\033[1;41m', (velocidade - 80) * 7, '\033[m'))
else:
    print('Você está dentro do limite de velocidade, Parabéns!')
