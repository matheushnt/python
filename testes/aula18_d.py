galera = list() # lista
dados = list()
maior_idade = menor_idade = 0
for pessoa in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])     # adicionando uma cópia da lista dados na lista pessoas 
    dados.clear()   # limpo o conteúdo da lista dados
for pessoa in galera:
    if pessoa[1] >= 18:
        print(f'{pessoa[0]} é maior de idade.')
        maior_idade += 1
    else:
        print(f'{pessoa[0]} é menor de idade.')
        menor_idade += 1
print(f'Há {maior_idade} pessoas maiores de idade.')
print(f'Há {menor_idade} pessoas menores de idade.')

"""
quando é adicionado uma lista dentro de outra lista é criado uma conexão entre elas, portanto qualquer alteração feita em uma lista também é alterado na outra lista
"""
 