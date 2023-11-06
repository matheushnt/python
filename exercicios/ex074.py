from random import random
print('~' * 30)
print('MENOR E MAIOR VALORES EM TUPLA')
print('~' * 30)
numeros = ((round(random() * 100), round(random() * 100), round(random() * 100),
           round(random() * 100), round(random() * 100)))
print(f'Os números sorteados foram: {numeros}')
print('-' * 30)
print(f'O menor número sorteado foi: {min(numeros)}')
print('-' * 30)
print(f'O maior número sorteado foi: {max(numeros)}')
print('-' * 30)
print(f'A soma de todos os valores da tupla é igual a {sum(numeros)}')
