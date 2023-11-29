matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_terceira_coluna = maior_valor_segunda_coluna= 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para ({linha}, {coluna}): '))
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
        if linha == 0 and coluna == 2 or linha == 1 and coluna == 2 or linha == 2 and coluna == 2:
            soma_terceira_coluna += matriz[linha][coluna]
        maior_valor_segunda_coluna = matriz[0][1]
        if matriz[1][1] > maior_valor_segunda_coluna:
            maior_valor_segunda_coluna = matriz[1][1]
        if matriz[2][1] > maior_valor_segunda_coluna:
            maior_valor_segunda_coluna = matriz[2][1]
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print('= =' * 15)
print(f'A soma de todos os valores digitados é igual a {soma_pares}')
print(f'A soma dos valores da terceira coluna é igual a {soma_terceira_coluna}')
print(f'O maior valor da segunda coluna é {maior_valor_segunda_coluna}')
