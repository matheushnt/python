print('-' * 30)
print('Sequência Fibonacci')
print('-' * 30)
n = int(input('Quantos termos você quer mostrar?\n'))
t1 = 0
t2 = 1
print('~' * 30)
print(f'{t1} ➞  {t2}', end='')
inicial = 3     # inicialização
while inicial <= n:     # teste lógico
    t3 = t1 + t2
    print(f' ➞  {t3}', end='')
    t1 = t2
    t2 = t3
    inicial += 1    # incremento
print(' ➞  FIM')
