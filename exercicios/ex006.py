#           PRIMEIRA RESOLUÇÃO
# num = int(input('Digite um número: '))    # lê a entrada de dados
# print(f'O dobro de {num} é {num * 2}. O triplo de {num} é {num * 3}. E, a raiz quadrada de {num} é {num**(1/2)}')     # efetua os cálculos e exibe a resposta

# a raiz quadrada é uma exponenciação, para encontrar a raiz quadrada de um número também pode elevá-lo a 1/2 (ou 0.5)


#           SEGUNDA RESOLUÇÃO
import math     # importando o módulo math
num = int(input('Digite um número: '))      # lê a entrada de dados
print(' Dobro: {} \n Triplo: {} \n Raiz quadrada: {:.0f}'.format(num * 2, num * 3, math.sqrt(num)))     # efetua os cálculos e exibe a resposta

# a função math.sqrt() é utilizada para encontrar a raiz quadrada de um número