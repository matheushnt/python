estado = dict()     # declarando um dicionário
brasil = list()     # declarando uma lista
for cont in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))   # adiciona um par chave-valor
    estado['sigla'] = str(input('Sigla do Estado: '))   # adiciona um par chave-valor
    brasil.append(estado.copy())    # adiciona uma cópia do dicionário
for estado in brasil:   # laçp para percorrer a lista
    for chave, valor in estado.items():     # laço para percorrer o dicionário
        print(f'O campo {chave} tem valor {valor}')
        print('- -' * 10)
for estado in brasil:   # laço para exibir apenas os valores do dicionário
    for valor in estado.values():
        print(f'{valor},', end=' ')
    print()
    