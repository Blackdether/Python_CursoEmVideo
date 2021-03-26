from random import randint
from time import sleep
pensar = randint(0, 5) # faz o computador escolher um número aleatório na lista
print('-=-'*24)
print('\033[35mVou pensar em um número entre 0 e 5. Tente adivinhar.....')
print('-=-'*24)
numeroEscolhido = int(input('\033[7mEm que número pensei? ')) # usuário tenta adivinhar o número
print('Estou pensando.....')
sleep(2) # O programa espera 2 segundos para continuar
if numeroEscolhido == pensar :
    print('\033[36mParabéns você acertou')
else:
    print('\033[1;31mVocê errou Seya seu viadinho, eu pensei no número {}'.format(pensar))
