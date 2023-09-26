print('\033[0;36m------ CONVERSOR DE BASES NUMÉRICAS  ------\033[m')
from time import sleep

num = int(input('Digite um número: '))
base = int(input('Digite 1 para converter em binário. \nDigite 2 para converter em octal. \nDigite 3 para converter em hexadecimal\n'))
print('PROCESSANDO...')
sleep(2)
if base == 1:
    conversao = bin(num)[2:]        # converte para base binária
elif base == 2:
    conversao = oct(num)[2:]        # converte para base octal
elif base == 3:
    conversao = hex(num)[2:]        # converte para base hexadecimal
else:
    print('Número inválido')
print(f'O número {num} convertido para a base {base} é {conversao}')
print('\033[0;31m------ FIM ------\033[m')
