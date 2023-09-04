# n1 = int(input('Um valor; '))   # lê a entrada de dados
# n2 = int(input('Outro valor: '))    # lê a entrada de dados
# print('A soma vale {}'.format(n1 + n2))     # exibe a resposta

# nesse caso não foi necessário criar uma variável para armazenar a soma entre N1 e N2, seria necessário quando fosse preciso o valor da soma posteriormente

n1 = int(input('Digite um valor: '))    # lê a entrada de dados
n2 = int(input('Digite outro valor: '))      # lê a entrada de dados
s = n1 + n2
m = n1 * n2
d = n1 / n2
d_i = n1 // n2
e = n1 ** n2
print(f'A soma é {s}, o produto é {m} e a divisão é {d:.1f}',end='. ')
print(f'A divisão inteira é {d_i} e a potência é {e}')

# para determinar a quantidade de casas decimais de um número, utiliza ":.2f" em que 2f determina a quantidade de casas podendo ser alterado

# para adicionar quebra de linha na função print(), utiliza-se \n

# para não ter uma quebra de linha entre duas funções print(), utiliza-se ", end='' "