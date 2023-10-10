print('\033[1;35m------ NÚMEROS PRIMOS ------\033[m')
numero = int(input('Digite um número: '))
total = 0   # receberá quantas vezes o número é dividido
for contador in range(1, numero+1):
    if numero % contador == 0:  # verifica se um número é primo ou não
        print('\033[1;33m', end=' ')
        total += 1  # recebe o números de vezes que é dividido o número
    else:
        print('\033[m', end=' ')
    print(contador, end=' ')
if total == 2:
    print(f'\n\033[m{numero} é um número primo.')
else:
    print(f'\n\033[mO número {numero} foi dividido {total} vezes. Por conta disso, não é um número primo.')
print('\033[1;35m------ FIM ------\033[m')
