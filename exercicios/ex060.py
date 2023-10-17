from time import sleep
from math import factorial
print('\033[1;34m******** CÁLCULO DE FATORIAL ********\033[m')
# calculando de forma de progressiva
num = int(input('Digite um número para calcular seu fatorial: '))
fatorial = 1
incr = 1    # inicialização
while incr <= num:  # enquanto meu número inicial for menor que número digitado pelo usuário, executa o laço
    fatorial *= incr    # multiplica o fatorial a cada nova iteração
    incr += 1   # incremento
print('CALCULANDO...')
sleep(1)
print(f'O valor de {num}! é igual a {fatorial}')

print('=-' * 20)

# Segunda forma de calcular fatorial utilizando o método factorial()
fat = int(input('Digite um número para calcular o seu fatorial: '))
print('CALCULANDO...')
sleep(1)
print(f'O fatorial de {fat}! é igual a {factorial(fat)}')   # o método factorial do módulo math, calcula o fatorial de um número

print('=-' * 20)

# calculando de forma regressiva
n = int(input('Digite um número para calcular o seu Fatorial: '))
c = n   # contador
f = 1   # fator nulo
while c > 0:
    print(c, end=' ')
    print('x' if c > 1 else '=', end=' ')
    f *= c  # calcula o fatorial
    c -= 1  # decrementa
sleep(1)
print(f)
print('\033[1;33m******** FIM ********\033[m')
