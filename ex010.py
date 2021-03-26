real = float(input('Digite quanto de dinheiro você tem? R$'))
dolar = real / 5.57
euro = real / 6.73
iene = real * 19.34
print('\033[1mCom R${} você pode comprar US${:.2f},Є{:.2f} e ¥{:.2f}'.format(real, dolar, euro, iene))
