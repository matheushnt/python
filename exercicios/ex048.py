
from time import sleep
soma = 0 
for contador in range(1, 501):
    if (contador % 2 != 0) and contador % 3 == 0:       # verifica se o número é ímpar e múltiplo de três
        print(f'O número {contador} é ímpar e múltiplo de três.')
        soma += contador
        sleep(0.05)
print(f'A soma entre todos os números ímpares múltiplos de 3 é igual a {soma}')
