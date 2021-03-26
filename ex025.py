nome = str(input('Digite seu nome: ')).strip()
temSilva = 'SILVA' in nome.upper().split()
print('Seu nome é \033[43m{}\033[m e você {} Silva'.format(nome, temSilva))
