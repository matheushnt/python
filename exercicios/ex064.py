print('=-' * 30)
print('TRATAMENTO DE VALORES')
print('=-' * 30)
numeros = 0
soma = 0
num = 0     # inicialização
num = int(input('Digite um número (999 para PARAR: '))
while num != 999:   # teste lógico
    soma += num     # soma os números digitados
    numeros += 1    # incremento
    num = int(input('Digite um número (999 para PARAR): '))
print('=-' * 30)
print(f'Programa finalizado com {numeros} números. Somando todos resultam em {soma}')
