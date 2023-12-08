print('+-'*15)
print(f'{'CADASTRO DE JOGADOR DE FUTEBOL':^30}')
print('+-'*15)
jogadores = []
jogador = {}
gols = []
while True:
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
    jogador['gols'] = gols[:]
    gols.clear()
    jogador['total'] = total
    jogadores.append(jogador.copy())
    resposta = str(input('Quer continuar [S/N] ?\n')).strip()[0]
    while resposta not in 'SsNn':
        resposta = str(input('Quer continuar [S/N] ?\n')).strip()[0]
    if resposta in 'Nn':
        break
print('='*40)
print(f'{'N°':<5}{'NOME':<12}{'GOLS':<8}{'TOTAL':>15}')
print('-'*40)
jogs = []
for i, jog in enumerate(jogadores):
    print(f'{i:<5}{jog['nome']:<12}{jog['gols']}{jog['total']:>20}')
    jogs.append(i)
print('-'*40)
while True:
    dados = int(input('Mostrar dados de qual jogador? (999 para PARAR): '))
    if dados == 999:
        break
    if dados in jogs:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[dados]['nome']}')
        for c, g in enumerate(jogadores[dados]['gols']):
            print(f'No jogo {c+1}, fez {g} gol(s).')
# todo: exibir uma mensagem de erro em caso do usuário solicitar os dados de um jogador inexistente