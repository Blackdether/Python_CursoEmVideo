from random import sample
# sample reorganiza os elementos, poderia utilizar SHUFFLE também

aluno1 = str(input('\033[4;7mDigite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
print('A ordem de apresentação dos alunos será: \n{}'.format(sample(lista, k=4)))
# k = quantos dos elementos dentro da lista serão embaralhados
