nome = str(input('\033[1;41mDigite seu nome completo: ')).strip()
print('Seu nome com todas as letras maiúsculas fica {}'.format(nome.upper()))
print('Seu nome com todas as letras minúsculas fica {}'.format(nome.lower()))
print('A quantidade de letras no seu nome é {}'.format(len(nome) - nome.count(' ')))
print('Seu primeiro é {} e ele tem {} letras'.format(nome.split()[0], len(nome.split()[0])))
# print('Seu primeiro tem {} letras'.format(nome.find(' ')))
# vai encontrar o primeiro espaço e identificar sua posição
# ex.: pedro aaa  --> 0p,1e,2d,3r,4o,5 , find vai gerar 5
