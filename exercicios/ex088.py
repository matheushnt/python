from random import randint
print('= ='* 10)
print(f'{'MEGA SENA':^30}')
print('= ='* 10)
jogadas = []
sorteio = []
jogos = int(input('Quantas jogadas você fará?\n'))
print(f'-=-=-=-= SORTEANDO {jogos} JOGOS =-=-=-=-')
for cont in range(0, jogos):    # laço para gerar a quantidade de jogos pedidos
    cont = 0
    while True: # laço para gerar 6 números aleatórios diferentes para cada jogo
        num = randint(0, 60)
        if num not in sorteio:
            sorteio.append(num)
            cont += 1
        if cont == 6:
            break
    jogadas.append(sorteio[:])  # adiciona uma cópia de cada jogo na lista jogadas
    sorteio.clear()
for posicao, jogo in enumerate(jogadas):
    print(f'Jogo {posicao+1}: {jogadas[posicao]}')
print(f'=-=-=-=-={' < BOA SORTE! > ':^5}=-=-=-=-=')    
 