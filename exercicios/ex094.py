print('=-'*15)
print(f'{'UNINDO DICIONÁRIOS E LISTAS':^30}')
print('=-'*15)
pessoas = []    # lista para armazenar os dicionários
pessoa = {}     # dicionário para armazenar os dados de cada pessoa
mulheres = []   # armazena as mulheres registradas
total = soma_idade = 0  # registra a quantidade de pessoas e soma as idades informadas para calcular a média posteriormente
while True:
    pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
    pessoa['idade'] = int(input('Idade: '))
    soma_idade += pessoa['idade']
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    pessoas.append(pessoa.copy())   # adiciona o dicionário com os dados da pessoa na lista principal
    total += 1  # contabiliza o registro da pessoa
    """ questiona se o usuário quer continuar  """
    resposta = str(input('Quer continuar [S/N]?\n')).strip()[0]
    while resposta not in 'SsNn':
        resposta = str(input('Quer continuar [S/N]?\n')).strip()[0]
    print('='*40)
    if resposta in 'Nn':
        break
print(f'Foram registradas {total} pessoas.')
print('-'*40)
media_idade = soma_idade / total    # calcula a média de idades
print(f' • A média de idade do grupo é igual a {media_idade:.2f}')
print('-'*40)
print(f' • As mulheres cadastradas foram: ', end='')
for mulher in mulheres:
    print(mulher, end=' ')
print()
print('-'*40)
print(' • Lista das pessoas acima da média:')
for dados in pessoas:   # laço FOR para iterar na lista principal
    for chave, valor in dados.items():  # laço FOR para iterar em cada dicionário
        if dados['idade'] > media_idade:
            print(f' - {chave}: {valor}', end=' ')
            print()
