from time import sleep
print('\033[1;35m------ SOMA DOS PARES ------\033[m')
soma = 0
for contador in range(1, 7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        soma += num
print('PROCESSANDO...')
sleep(0.05)
print(f'A soma entre os valores apenas pares são: {soma}')
print('\033[1;34m------ FIM ------\033[m')
