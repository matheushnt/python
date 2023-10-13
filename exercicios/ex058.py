from random import random
from time import sleep
print('\033[1;35m=-=-=- JOGO DA ADIVINHAÇÃO 2.0 -=-=-=\033[m')
maquina = round(random() * 10)       # gera um número aleatório entre 0 e 10
print('Pensei em um número, tente adivinhar qual é...')
palpite = int(input('Dê o seu palpite: '))
tentativas = 1      # contabiliza o número de tentativas
print('PROCESSANDO...')
sleep(0.7)
while palpite != maquina:   # se a tentativa for diferente do número da máquina, executa o laço
    if palpite < maquina:
        palpite = int(input('Mais... Tente novamente: '))
        print('PROCESSANDO...')
        sleep(0.7)
    if palpite > maquina:
        palpite = int(input('Menos... Tente novamente: '))
        print('PROCESSANDO...')
        sleep(0.7)
    tentativas += 1     # incrementa no número de tentativas
if tentativas == 1:
    print(f'Eu pensei no número {maquina}. Você acertou de primeira. Parabéns, com essa sorte, pode jogar na Mega Sena da Virada.')
else:
    print(f'Eu pensei no número {maquina}. Você acertou na {tentativas}° tentativa. Parabéns.')
print('\033[1;36m=-=-=- FIM -=-=-=\033[m')
