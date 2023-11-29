matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_terceira_coluna = maior_valor_segunda_coluna= 0
""" LAÇOS FOR PARA ALIMENTAR A MATRIZ """
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para ({linha}, {coluna}): '))
        if matriz[linha][coluna] % 2 == 0:  # condição para verificar se o número é par
            soma_pares += matriz[linha][coluna]
""" LAÇOS FOR PARA TABULAR MINHA MATRIZ """
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print('= =' * 15)
print(f'A soma de todos os valores pares digitados é igual a {soma_pares}')
for linha in range(0, 3):   # laço para somar todos os valores da terceira coluna
    soma_terceira_coluna += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é igual a {soma_terceira_coluna}') 
for cont in range(0, 3):    # laço para verificar qual é o maior valor da segunda coluna
    if cont == 0 or matriz[cont][1] > maior_valor_segunda_coluna:
        maior_valor_segunda_coluna = matriz[cont][1] 
print(f'O maior valor da segunda coluna é {maior_valor_segunda_coluna}')
