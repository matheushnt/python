from time import sleep
valores = []
print('-'*30)
print(f'{'VALORES ÚNICOS EM UMA LISTA':^30}')
print('-'*30)
while True: # loop infinito
    valor = int(input('Digite um número: '))
    if valor not in valores:    # se o valor digitado não estiver em na lista valores, será adicionando na lista
        valores.append(valor)   # valor adicionado
    else:   # não será adicionado 
        print('Valor já adicionado!')
    print('-'*30)
    resposta = str(input('Quer continuar? [S/N]\n'))[0]     # pergunta se o usuário quer continuar a adicionar números
    while resposta not in 'SsNn':   # se a resposta for diferente de S/N, dispará o loop
        resposta = str(input('Quer continuar? [S/N]\n'))[0]
    if resposta in 'Nn':    # se a resposta a pergunta for negativa, o usuário irá parar de adicionar números
        break   # interrompe o loop infinito
print('PROCESSANDO...')
sleep(2)
print(f'Valores adicionados: {sorted(valores)}')    # exibe a lista organizada de forma crescente
