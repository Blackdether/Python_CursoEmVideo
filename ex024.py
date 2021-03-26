cidade = str(input('Digite o nome da sua cidade: ')).strip()
divNome = cidade.upper().split()
comSanto = 'SANTO' in divNome[0]
print('\033[41mSua cidade começa com Santo?: {}'.format(comSanto))
