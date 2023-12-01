estudante = {}  # dicionário vazio
estudante['Nome'] = str(input('Nome: '))    # Adicionando um item
estudante['Média'] = float(input('Média: '))    # Adicionando um item
# dependendo da média, terá um valor diferente para a nova chave a ser adicionada
if estudante['Média'] < 7:
    estudante['Situação'] = 'Reprovado'
else:
    estudante['Situação'] = 'Aprovado'
for chave, valor in estudante.items():  # laço para percorrer no dicionário
    print(f'{chave} é igual a {valor}')
