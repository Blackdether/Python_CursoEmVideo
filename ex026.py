frase = str(input('\033[33;1mDigite uma frase: ')).strip().lower()
quantosA = frase.count('a')
primeiraPosi = frase.find('a') + 1
ultimaPosi = frase.rfind('a') + 1
print('\033[36mA letra a aparece {} vezes'.format(quantosA))
print('A letra a aparece pela primeira vez na posição {} '.format(primeiraPosi))
print('A letra a aparece pela última vez na posição {}'.format(ultimaPosi))
