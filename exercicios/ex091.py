from random import randint
from time import sleep
jogadores = {}  # declarando um dicionário vazio
jogadores['jogador1'] = randint(1, 6)
jogadores['jogador2'] = randint(1, 6)
jogadores['jogador3'] = randint(1, 6)
jogadores['jogador4'] = randint(1, 6)
print('Valores sorteados:')
for chave, valor in jogadores.items():  # acessando as chaves e valores do dicionário
    print(f'    O {chave} tirou {valor}')
    sleep(1)
cont = 1
print('Ranking dos Jogadores:')
for chave in sorted(jogadores, key=jogadores.get, reverse=True):
    print(f'    {cont}° lugar: {chave} com {jogadores[chave]}')
    cont +=1
    sleep(1)
# sorted(jogadores, key=jogadores.get, reverse=True) => comando para ordenar de forma decrescente o dicionário    
