print('-' * 40)
print(f'{'LISTA COMPOSTA E ANÁLISE DE DADOS':^40}')
print('-' * 40)
pessoas = [[], []]  # lista composta, cada lista dentro da lista principal possui entrada de dados diferentes
pessoa_pesada = []  # armazena quais pessoas são as mais pesadas
pessoa_leve = []    # armazena quais pessoas são as mais leves
contador_pessoas = maior = menor = 0
while True:
    pessoas[0].append(str(input('Nome: ')))
    pessoas[1].append(float(input('Peso: ')))
    contador_pessoas += 1   # conta quantas pessoas foram cadastradas
    print('-' * 40)
    resposta = str(input('Quer continuar? [S/N]\n'))[0].strip()
    while resposta not in 'SsNn':
        resposta = str(input('Quer continuar? [S/N]\n'))[0].strip()
    if resposta in 'Nn':
        break
    print('-' * 40)
print(f'Foram cadastradas {contador_pessoas} pessoas.')
for indice, peso in enumerate(pessoas[1]):  # percorre a lista de pesos informados, retornando o índice de cada um
    """ Verificação do maior e menor peso de cada pessoa """
    if indice == 0:
        maior = menor = peso
        pessoa_pesada = pessoa_leve = pessoas[0][indice]
    if peso > maior:
        maior = peso
        pessoa_pesada = pessoas[0][indice]
    if peso < menor:
        menor = peso
        pessoa_leve = pessoas[0][indice]
""" Informações acerca do peso das pessoas """
print(f'O maior peso foi de {maior}. Peso de ', end=' ')
for indice, peso_pesado in enumerate(pessoas[1]):
    if maior == peso_pesado:
        print(f'{pessoas[0][indice]},', end=' ')
print(f'\nO menor peso foi de {menor}. Peso de ', end=' ')
for indice, peso_leve in enumerate(pessoas[1]):
    if menor == peso_leve:
        print(f'{pessoas[0][indice]},', end=' ')
