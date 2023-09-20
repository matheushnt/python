print('=== PAR ou ÍMPAR ===')
print('PAR ou ÍMPAR')
num = int(input('Digite um número: '))
resto = num % 2     # armazena o resto da divisão
if resto == 0:      # verifica se o resto é igual a zero, caso seja, retorna par, senão, ímpar
    print(f'{num} é PAR')
else:
    print(f'{num} é ÍMPAR')
print('===== FIM =====')
