print('+-'*15)
print(f'{'CADASTRO DE JOGADOR DE FUTEBOL':^30}')
print('+-'*15)
jogador = {}    # dicionário que armazena os dados do jogador
gols = []   # armazena os números de gols
jogador['nome'] = str(input('Nome do Jogador: ')).strip()
print('-'*30)
partidas = int(input(f'Quantas partidas {jogador['nome']} jogou?\n'))
print('-'*30)
for cont in range(0, partidas): # questiona quantos gols o jogador fez em cada partida e os armazena 
    gols.append(int(input(f'Quantos gols na partida {cont+1}?\n')))
print('-'*30)
total = 0
for gol in gols:    # laço que itera dentro da lista de gols
    total += gol    # somatória de gols
jogador['gols'] = gols  # a lista gol é adicionada a uma chave do dicionário
jogador['total'] = total    # o total de gols é adicionado a uma chave do dicionário
for chave, valor in jogador.items():
    print(f'{chave}: {valor}')
print('-'*30)
print(f'O jogador {jogador['nome']} jogou {partidas} partidas')
total_gols = 0
for cont, gols in enumerate(jogador['gols']):   # laço que itera dentro do valor (que é a lista de gols)
    print(f'  → Na partida {cont+1}, fez {gols} gol(s).')
print(f'Foi um total de {total}')
