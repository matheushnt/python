from random import randint
""" ITERAÇÕES FOR DENTRO DE LISTAS """
numeros = []    # lista vazia
for contador in range(1, 6):
    numeros.append(randint(0, 10))  # adicionando valores aleatórios a cada nova iteração
for posicao, numero in enumerate(numeros):
    print(f'Na posição {posicao}, foi encontrado o valor {numero}')

print('=-'*30)
print('=-'*30)

valores = list()    # lista vazia
for pergunta in range(0, 5):
    valores.append(int(input('Digite um número: ')))    # adicionando valores na lista através de um input()
for posicao, pergunta in enumerate(valores):
    print(f'Na posição {posicao}, foi encontrado o valor {pergunta}')
