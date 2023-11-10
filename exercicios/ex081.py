from time import sleep  # importação apenas do método sleep()
numeros = []    # lista vazia
print('*'*40)
print(f'{'EXTRAINDO DADOS DE UMA LISTA':^40}')
print('*'*40)
while True: # laço infinito
    num = int(input('Digite um número: '))
    print('-'*30)
    numeros.append(num)     # adiciona o valor digitado na lista
    resposta = str(input('Quer continuar? [S/N]\n'))[0].strip()     # questiona se o usuário quer continuar 
    while resposta not in 'SsNn':   # caso, digite diferente do esperado, dispara um laço
        resposta = str(input('Quer continuar? [S/N]\n'))[0].strip()
    if resposta in 'Nn':    # se a resposta for negativa, interrompe o laço
        break   # comando para interromper o laço
    print('~'*30)
print('PROCESSANDO...')
sleep(2)    # interrompe a execução do programa por 2 segundos
print('='*40)
print(f'Foram digitados {len(numeros)} números')    # quantos quantos números foram digitados
print(f'Os valores organizados de forma decrescente: {sorted(numeros, reverse=True)}')  # exibe a lista organizada de forma decrescente
if 5 in numeros:    # se 5 fizer parte da lista, será retornado que o valor está contido
    print('O valor 5 está na lista')
else:   # caso contrário, retorna que não faz parte 
    print('O valor 5 não está na lista')
