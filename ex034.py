salario = float(input('Digite seu salário: R$'))
if salario > 1250 :
    aumento = salario * (1 + 10 / 100)
else:
    aumento = salario * (1 + 15 / 100)
print('{}Seu novo salário é de R${:.2f}'.format('\033[1;36m' ,aumento))
