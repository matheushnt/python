from time import sleep
print('\033[4;35m=-=-=- SOMA DE ÍMPARES E MÚLTIPLOS DE TRÊS -=-=-=\033[m')
soma = 0    # acumulador 
for contador in range(1, 501, 2):
    # verifica se o número é ímpar e múltiplo de três
    if contador % 3 == 0:
        print(f'O número {contador} é ímpar e múltiplo de três.')
        soma += contador    # acumulador
        sleep(0.05)
print(f'A soma entre todos os números ímpares múltiplos de 3 é igual a {soma}')
print('\033[4;35m=-=-=- FIM -=-=-=\033[m')
