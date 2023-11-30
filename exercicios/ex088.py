from random import randint
print('= ='* 10)
print(f'{'MEGA SENA':^30}')
print('= ='* 10)
jogadas = []
sorteio = []
jogos = int(input('Quantas jogadas você fará?\n'))
print(f'-=-=-=-= SORTEANDO {jogos} JOGOS =-=-=-=-')
for cont in range(0, jogos):
    cont = 0
    while True:
        num = randint(0, 60)
        if num not in sorteio:
            sorteio.append(num)
            cont += 1
        if cont == 6:
            break
    jogadas.append(sorteio[:])
    sorteio.clear()
for posicao, jogo in enumerate(jogadas):
    print(f'Jogo {posicao+1}: {jogadas[posicao]}')
print(f'=-=-=-=-={' < BOA SORTE! > ':^5}=-=-=-=-=')    
 