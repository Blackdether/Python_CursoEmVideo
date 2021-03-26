digitado = input('Digite algo: ')
print('\033[4mO tipo primitivo desse valor é \033[35m{}\033[m, é numérico?: {}, é alfabético?: {}, é alfanumério?: {}, é um digito?: {}, Está em maiúsculas?: {},esta em minúsculas?: {}'.format(type(digitado), digitado.isnumeric(), digitado.isalpha(), digitado.isalnum(), digitado.isdigit(), digitado.isupper(), digitado.islower()))
