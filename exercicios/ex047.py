from time import sleep
print('\033[1;31m****** CONTAGEM DE PARES ******\033[m')
for numPar in range(1, 51):     # o loop vai de 1 a 50, ignorando o 51
    if numPar % 2 == 0:     # verifica se o número é par, se sim, é exibido na tela
        print(f'O numero {numPar} é par')
        sleep(0.1)
print('Fim do Loop')
print('\033[1;36m****** FIM ******\033[m')
