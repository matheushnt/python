print('+-'*15)
print(f'{'CADASTRO DE JOGADOR DE FUTEBOL':^30}')
print('+-'*15)
jogador = {}
gols = []
jogador['nome'] = str(input('Nome do Jogador: ')).strip()
print('-'*30)
partidas = int(input(f'Quantas partidas {jogador['nome']} jogou?\n'))
print('-'*30)
for cont in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {cont+1}?\n')))
print('-'*30)
total = 0
for gol in gols:
    total += gol
jogador['gols'] = gols
jogador['total'] = total
for chave, valor in jogador.items():
    print(f'{chave}: {valor}')
print('-'*30)
print(f'O jogador {jogador['nome']} jogou {partidas} partidas')
total_gols = 0
for cont, gols in enumerate(jogador['gols']):
    print(f'  → Na partida {cont+1}, fez {gols} gol(s).')
print(f'Foi um total de {total}')
