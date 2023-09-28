from random import choice
from time import sleep
print('\033[1;36m*=*=*=* JOKENPÔ *=*=*=*\033[m')
jogo = str(input('Escolha Pedra, Papel ou Tesoura:\n')).capitalize().strip()        # capitaliza os dados inseridos e apaga os espaços em branco inúteis.
opcoes = ['Pedra', 'Papel', 'Tesoura']      # armazena as opcões do jogo Jokenpô
maquina = choice(opcoes)        # essa variável armazena uma opcão aleatória gerada pelo método choice()
print('JO')
sleep(0.8)
print('KEN')
sleep(0.8)
print('PÔ')
sleep(0.8)
print(f'A Máquina jogou {maquina}')
sleep(0.8)
if jogo == maquina:
    print('Ninguém ganhou.')
elif jogo == 'Pedra' and maquina == 'Papel':
    print('Papel encobre Pedra.')
    sleep(0.8)
    print('A Máquina venceu')
elif jogo == 'Papel' and maquina == 'Tesoura':
    print('Tesoura corta Papel.')
    sleep(0.8)
    print('A Máquina venceu.')
elif jogo == 'Tesoura' and maquina == 'Pedra':
    print('Pedra quebra Tesoura.')
    sleep(0.8)
    print('A Máquina venceu.')
elif jogo == 'Papel' and maquina == 'Pedra':
    print('Papel encobre Pedra.')
    sleep(0.8)
    print('O jogador venceu.')
elif jogo == 'Tesoura' and maquina == 'Papel':
    print('Tesoura corta Papel.')
    sleep(0.8)
    print('O jogador venceu.')
elif jogo == 'Pedra' and maquina == 'Tesoura':
    print('Pedra quebra Tesoura.')
    sleep(0.8)
    print('O jogador venceu.')
print('\033[0;35m*=*=*=* FIM *=*=*=*\033[m')
