precoOriginal = float(input('Digite o preço do produto: R$'))
desconto = int(input('Digite qual a % de desconto: '))
precoNovo = (1 - desconto/100) * precoOriginal
print('{}O seu produto, com desconto de {}%, vai custar R${:.2f}'.format('\033[43m', desconto, precoNovo))
