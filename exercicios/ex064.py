print('=-' * 30)
print('TRATAMENTO DE VALORES')
print('=-' * 30)
numeros = 0
soma = 0
num = 0     # inicialização
while num != 999:   # teste lógico
    num = int(input('Digite um número (999 para PARAR): '))
    soma += num     # soma os números digitados
    numeros += 1    # incremento
print('=-' * 30)
print(f'Programa finalizado com {numeros - 1} números. Somando todos resultam em {soma - 999}')
