from random import randint
jogadas = []
sorteio = []
jogos = int(input('Quantas jogadas você fará?\n'))
for cont in range(0, jogos):
    inicio = 0
    while inicio < 6:
        sorteio.append(randint(0, 60))
        jogadas.append(sorteio[:])
        sorteio.clear()
        inicio += 1
print(jogadas)
