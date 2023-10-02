from time import sleep
print('\033[4;35m****** CONTAGEM REGRESSIVA ******\033[m')
print('Contagem regressiva para a decolagem do Foguete.')
for regressiva in range(10, 0, -1):     # loop for para efetuar a contagem regressiva
    print(regressiva)
    sleep(1)
print('Decolagem feita com sucesso.')
print('\033[4;36m****** FIM ******\033[m')
