viagemDistancia = float(input('Digite a distância da viagem em Km: '))
if viagemDistancia <= 200 :
    preco = 0.5 * viagemDistancia
else:
    preco = 0.45 * viagemDistancia
print('Sua viagem é de {:.1f}Km e o preço da passagem é R${:.2f}'.format(viagemDistancia, preco))
