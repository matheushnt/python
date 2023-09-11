from math import factorial      # importando somente a função factorial do módulo math
num = int(input('Digite um número: '))
fat = factorial(num)        # utilizando a função factorial() 
print(f'O fatorial de {num} é igual a {fat}')