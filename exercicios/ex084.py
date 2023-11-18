pessoas = []
pessoa = []
maior = menor = contador_pessoas = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(int(input('Peso: ')))
    pessoas.append(pessoa[:])
    contador_pessoas += 1
    pessoa.clear()
    resposta = str(input('Quer continuar? [S/N]\n'))[0].strip()
    while resposta not in 'SsNn':
        resposta = str(input('Quer continuar? [S/N]\n'))[0].strip()
    if resposta in 'Nn':
        break
print(f'Foram cadastradas {contador_pessoas} pessoas.')

