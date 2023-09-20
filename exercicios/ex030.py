from time import sleep
print('=== PAR ou ÍMPAR ===')
num = int(input('Digite um número: '))
resto = num % 2     # armazena o resto da divisão
sleep(3)        # O método sleep suspende a execução pelo número de segundos informado em seu parâmetro
if resto == 0:      # verifica se o resto é igual a zero, caso seja, retorna par, senão, ímpar
    print(f'{num} é PAR')
else:
    print(f'{num} é ÍMPAR')
print('===== FIM =====')
