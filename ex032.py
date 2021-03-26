from datetime import date
ano = int(input('Digite em que ano você está ou coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year # Pega o ano atual
if (ano % 4 == 0) and (ano % 100 != 0) or (ano // 400 == 0):
    print('\033[35mO ano de {} é BISSEXTO'.format(ano))
else:
    print('\033[36mO ano de {} NÃO É BISSEXTO'.format(ano))
