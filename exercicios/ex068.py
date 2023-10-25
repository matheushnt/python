from random import randint
print('=-' * 30)
print(f'{'VAMOS JOGAR PAR OU ÍMPAR':^60}')
print('=-' * 30)
vitorias = 0    # soma a quantidade de vitórias
while True:     # laço infinito enquanto o jogador não perder
    jogador = int(input('Diga um número: '))
    opcao = str(input('Par ou Ímpar?\n')).strip()[0]
    computador = randint(0, 50)
    print('-' * 60)
    if opcao in 'Pp':   # se for par
        if (jogador + computador) % 2 == 0:     # verifica se é par o número
            print(f'Você jogou {jogador} e o computador {computador}. No total deu {jogador + computador} que é PAR')
            print('-' * 60)
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            vitorias += 1   # incrementa na variável vitórias
            print('~' * 60)
        else:       # senão é ímpar
            print(f'Você jogou {jogador} e o computador {computador}. No total deu {jogador + computador} que é ÍMPAR.')
            print('-' * 60)
            print('Você PERDEU!')
            print('-' * 60)
            print(f'GAME OVER! Você venceu {vitorias} vezes.')
            break   # interrompe o laço se o jogador perder

    if opcao in 'ÍIíi':     # se for ímpar
        if (jogador + computador) % 2 != 0:     # verifica se é ímpar o número
            print(f'Você jogou {jogador} e o computador {computador}. No total deu {jogador + computador} que é ÍMPAR')
            print('-' * 60)
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            vitorias += 1   # incrementa na variável vitórias
            print('~' * 60)
        else:       # senão é íar
            print(f'Você jogou {jogador} e o computador {computador}. No total deu {jogador + computador} que é PAR.')
            print('-' * 60)
            print('Você PERDEU!')
            print('-' * 60)
            print(f'GAME OVER! Você venceu {vitorias} vezes.')
            break   # interrompe o laço se o jogador perder
