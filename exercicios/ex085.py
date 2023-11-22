print('= ='*10)
print(f'{'LISTAS COM PARES E ÍMPARES':^30}')
print('= ='*10)
numeros_analisados = [[], []]
for cont in range(0, 10):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        numeros_analisados[0].append(num)
        numeros_analisados[0].sort()
    else:
        numeros_analisados[1].append(num)
        numeros_analisados[1].sort()
    print('-'*30)
if len(numeros_analisados[0]) == 0:
    print('Não foi registrado nenhum número par.')
else:
    print('Os números pares cadastrados foram: ', end=' ')
    for valor in numeros_analisados[0]:
        print(f'{valor}', end=' ')
print('\n- - - - - - - - - - - - - - - - - - - - - - - - -')
if len(numeros_analisados[1]) == 0:
    print('Não foi registrado nenhum número ímpar.')
else:
    print('Os números ímpares cadastrados foram: ', end=' ')
    for valor in numeros_analisados[1]:
        print(f'{valor}', end=' ')
print('\n= = = = = = = = = = = = FIM = = = = = = = = = = = =', end='')
