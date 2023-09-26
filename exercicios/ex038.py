print('\033[0;33m****** COMPARANDO NÚMEROS ******\033[m')
from time import sleep
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print('PROCESSANDO...')
sleep(2)
if n1 > n2:
    print(f'{n1} é maior que {n2}')
elif n2 > n1:
    print(f'{n2} é maior que {n1}')
else:
    print('Os dois valores são iguais.')
print('\033[0;33m****** FIM ******\033[m')
