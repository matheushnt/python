pessoas = []
pessoa = {}
mulheres = []
total = soma_idade = 0
while True:
    pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
    pessoa['idade'] = int(input('Idade: '))
    soma_idade += pessoa['idade']
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    pessoas.append(pessoa.copy())
    total += 1
    resposta = str(input('Quer continuar [S/N]?\n')).strip()[0]
    while resposta not in 'SsNn':
        resposta = str(input('Quer continuar [S/N]?\n')).strip()[0]
    if resposta in 'Nn':
        break
print(f'Foram registradas {total} pessoas.')
media_idade = soma_idade / total
print(f'A média de idade do grupo é igual a {media_idade:.2f}')
print(f'As mulheres cadastradas foram: ', end='')
for mulher in mulheres:
    print(mulher, end=' ')
print()
print('Lista das pessoas acima da média:')
for dados in pessoas:
    for chave, valor in dados.items():
        if dados['idade'] > media_idade:
            print(f'{chave}: {valor}', end=' ')
            print()