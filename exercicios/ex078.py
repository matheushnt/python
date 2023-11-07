from time import sleep
valores = list()    # lista vazia
print('*' * 60)
print(f'{'MAIOR E MENOR VALOR EM UMA LISTA':^60}')
print('*' * 60)
for contador in range(0, 5):
    valores.append(int(input('Digite um número: ')))    # será iterado um novo valor a cada input()
    print('=' * 40)
print(f'O maior número digitado foi {max(valores)}')
print('-' * 40)
print(f'O menor número digitado foi {min(valores)}')
print('-' * 40)
print('PROCESSANDO...')
print('-' * 40)
sleep(2)
for posicao, valor in enumerate(valores):   # retorna o conteúdo e seu índice
    print(f'O número {valor} encontra-se na posição {posicao + 1}')
    print('=-' * 20)
