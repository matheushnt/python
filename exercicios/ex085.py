numeros_analisados = [[], []]
for cont in range(0, 10):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        if cont == 0 or num > numeros_analisados[0][-1]:
            numeros_analisados[0].append(num)
        else:
            indice = 0
            while indice < len(numeros_analisados[0]):
                if num <= numeros_analisados[0][indice]:
                    numeros_analisados[0].insert(indice, num)
                    break
                indice += 1
    else:
        if cont == 0 or num > numeros_analisados[1][-1]:
            numeros_analisados[1].append(num)
        else:
            indice = 0
            while indice < len(numeros_analisados[1]):
                if num <= numeros_analisados[1][indice]:
                    numeros_analisados[1].insert(indice, num)
                    break
                indice += 1
print('Os números pares cadastrados foram: ', end=' ')
for valor in numeros_analisados[0]:
    print(f'{valor}', end=' ')
print('\nOs números ímpares cadastrados foram: ', end=' ')
for valor in numeros_analisados[1]:
    print(f'{valor}', end=' ')
