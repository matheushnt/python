print('PAR ou ÍMPAR')
num = int(input('Digite um número: '))
resto = num % 2
if resto == 0:
    print(f'{num} é PAR')
else:
    print(f'{num} é ÍMPAR')
    