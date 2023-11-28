print('+-' * 15)
print(f'{'MATRIZ EM PYTHON':^30}')
print('+-' * 15)
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# laços FOR para alimentar a matriz
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um número para [{linha}, {coluna}]: '))
# laços FOR para tabular as linhas e colunas
print('+-' * 15)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
