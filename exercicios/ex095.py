print('+-'*15)
print(f'{'CADASTRO DE JOGADOR DE FUTEBOL':^30}')
print('+-'*15)
jogadores = []  # lista que armazena todos os dicionários contendo informações de cada jogador
jogador = {}    # dicionário que irá conter as informações do jogador
gols = []       # todos os gols de cada jogador será contido nessa lista
jogs = []   # lista que irá armazena o código de busca de cada jogador
while True:
    jogador['nome'] = str(input('Nome do Jogador: ')).strip().capitalize()  # recebe o nome do jogador
    print('-'*30)
    partidas = int(input(f'Quantas partidas {jogador['nome']} jogou?\n'))   # recebe a quantidade de partidas do jogador
    print('-'*30)
    for cont in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {cont+1}?\n')))     # recebe e armazena na lista quantos gols em cada partida
    print('-'*30)
    total = 0   # totaliza os gols informados
    for gol in gols:    # laço para percorrer a lista de gols
        total += gol    # soma os gols
    jogador['gols'] = gols[:]   # adiciona uma cópia da lista de gols ao dicionário para que não ocorra uma conexão entre as listas
    gols.clear()    # limpa a lista de gols
    jogador['total'] = total    # recebe o total de gols
    jogadores.append(jogador.copy())    # adiciona uma cópia do dicionário na lista de jogadores
    resposta = str(input('Quer continuar [S/N] ?\n')).strip()[0]
    while resposta not in 'SsNn':
        resposta = str(input('Quer continuar [S/N] ?\n')).strip()[0]
    if resposta in 'Nn':
        break
print('='*45)
print(f'{'N°':<4}{'NOME':<11}{'GOLS':<15}{'TOTAL':>15}')
print('-'*45)
for i, jog in enumerate(jogadores):
    print(f'{i:<4}{jog['nome']:<11}{str(jog['gols']):<15}{jog['total']:>15}')
    jogs.append(i)  # o código de busca de cada jogador é adicionado a listagem
print('-'*45)
while True:
    dados = int(input('Mostrar dados de qual jogador? (999 para PARAR): '))
    if dados == 999:
        break
    if dados in jogs:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[dados]['nome']}')
        for c, g in enumerate(jogadores[dados]['gols']):
            print(f'No jogo {c+1}, fez {g} gol(s).')
    else:   # se o código de busca informado não estiver vinculado a um jogador, retornará um erro
        print('Jogador não registrado. Tente novamente. ', end='')
