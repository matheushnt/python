print('\033[0;33m-=--=--=- APROVANDO EMPRÉSTIMO -=--=--=-\033[m')
from time import sleep
casa = float(input('Qual o valor da casa?\n R$ '))
salario = float(input('Quanto você ganha de salário?\n R$ '))
anos = int(input('Em quantos anos você ficará pagando a casa?\n'))
mensalidade = casa / (anos * 12)        # calcula o preço da mensalidade 
minimo = salario * 30 / 100       # calcula 30% do salário
print('CALCULANDO...')
sleep(2)
if mensalidade > minimo:       # Caso a mensalidade seja maior do que 30% do salário, empréstimo negativado
    print(f'A mensalidade será R$ {mensalidade:.2f}')
    print('Infelizmente você não poderá fazer o empréstimo. A mensalidade não pode exceder 30' + "%" ' do seu salário')
else:       # empréstimo aprovado
    print(f'A mensalidade será R$ {mensalidade:.2f}')
    print('Empréstimo Aprovado.')
print('\033[0;31m=--=--=- FIM -=--=--=-\033[m')
