salario = float(input('Digite o seu salário atual: '))
aumento = int(input('Digite qual será a % do seu aumento: '))
novoSalario = (1 + aumento/100) * salario
print('\033[33mSeu novo salário, com aumento de {}%, será de R${:.2f}'.format(aumento, novoSalario))
