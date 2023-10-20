from statistics import mean
numeros = []
num = int(input('Digite um número: '))
numeros.append(num)
resp = str(input('Quer continuar? [SIM/NÃO]: ')).strip()[0]
if resp in 'SIMsim':
    while resp in 'Ss':
        num = int(input('Digite um número: '))
        numeros.append(num)
        resp = str(input('Quer continuar? [SIM/NÃO]: ')).strip()[0]
    media = mean(numeros)
    print('~' * 30)
    print(f'{'INFORMAÇÕES IMPORTANTES':^30}')
    print('~' * 30)
    print(f'O maior número digitado: {max(numeros)}')
    print('-' * 30)
    print(f'O menor número digitado: {min(numeros)}')
    print('-' * 30)
    print(f'A Média Aritmética: {media:.2f}')
    print('-' * 30)
    print(f'{'FIM':^30}')
    print('-' * 30)
else:   # se o usuário digitar diferente de zero, é exibido uma perguntar 
    print('Há poucos dados informados. Não há como fazer uma análise.')
    resp = str(input('Você gostaria de inserir mais dados?\n'))[0]
    if resp in 'Ss':
        while resp in 'SIMsim':
            num = int(input('Digite um número: '))
            numeros.append(num)
            resp = str(input('Quer continuar? [SIM/NÃO]: ')).strip()[0]
        media = mean(numeros)
        print('~' * 30)
        print(f'{'INFORMAÇÕES IMPORTANTES':^30}')
        print('~' * 30)
        print(f'O maior número digitado: {max(numeros)}')
        print('-' * 30)
        print(f'O menor número digitado: {min(numeros)}')
        print('-' * 30)
        print(f'A Média Aritmética: {media:.2f}')
        print('-' * 30)
        print(f'{'FIM':^30}')
        print('-' * 30)
    else:
        print('-' * 30)
        print('Tudo bem! Volte sempre.')
        print('-' * 30)
