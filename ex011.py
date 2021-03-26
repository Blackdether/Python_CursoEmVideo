altura = float(input('Digite qual a altura da parede: '))
largura = float(input('Digite qual a largura da parede: '))
area = altura * largura
litros = area/2
cores = {'azul':'\033[46m', 'nada':'\033[m'}
print('{}Sua parede tem a dimensão de {}x{} e sua área é de {:.3f}m2.{} \nPara pintar essa parede,você precisará de {:.4f}l de tinta.'.format(cores['azul'], largura, altura, area, cores['nada'], litros))
