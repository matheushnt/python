print('=-='*15)
print(f'{'DIVIDINDO VALORES EM VÁRIAS LISTAS':^45}')
print('=-='*15)
valores = list()    # lista vazia
while True: # laço infinito
    valor = int(input('Digite um número: '))
    valores.append(valor)   # valor digitado adicionado a lista
    resp = str(input('Quer continuar? [S/N]\n'))[0].strip()
    while resp not in 'SsNn':   # laço tem a função de validação da resposta do usuário
        resp = str(input('Quer continuar? [S/N]\n'))[0].strip()
    if resp in 'Nn':    # se a resposta for negativa, o laço infinito será interrompido
        break   # interrompe o laço infinito
pares = list()  # lista vazia
impares = list()    # lista vazia
for num in valores:     # percorre cada valor na lista
    if num % 2 == 0:    # se o valor for par, é adicionado a lista de pares
        pares.append(num)
    else:   # se o valor for ímpar, é adicionado a lista de ímpares
        impares.append(num)
print('=-='*15)
print(f'Lista completa: {valores}')     # exibe a lista completa
print(f'Lista de pares: {pares}')       # exibe a lista de pares
print(f'Lista de ímpares: {impares}')   # exibe a lista de ímpares
