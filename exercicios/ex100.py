from random import randint
from time import sleep


print('~'*30)
print(f'{'FUNÇÕES DE SORTEIO E SOMA':^30}')
print('~'*30)


def sorteio():  # Função que sorteia 5 números diferentes 
    print('-='*20)
    while len(numeros) != 5:
        num = randint(0, 100)
        if num not in numeros:  # Adiciona um número caso ainda não esteja na lista
            numeros.append(num)
    print('Números sorteados: ', end='')
    for n in numeros:
        print(n, end=' ', flush=True)
        sleep(0.4)
    print()


def soma_par(lst):  # Função que soma todos os números pares sorteados
    s = 0
    for valor in lst:
        if valor % 2 == 0:
            s += valor
    print(f'A soma dos valores pares sorteados: {s}')


""" PROGRAMA PRINCIPAL """
numeros = []
sorteio()
soma_par(numeros)
