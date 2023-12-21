from time import sleep

print('= -' * 10)
print(f'{'FUNÇÃO DE CONTADOR':^30}')
print('= -' * 10)


def contador(i, f, p):  # Definindo a função de contagem
    print('- -' * 10)
    if i < f:  # Caso o início seja menor que o fim, inicia a contagem progressiva
        print(f'Contagem de {i} até {f} de {p} em {p}')
        cont = i
        while cont <= f:
            print(cont, end=' ', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:  # Caso o início seja maior que o fim, inicia a contagem regressiva
        print(f'Contagem de {i} até {f} de {p} em {p}')
        cont = i
        while cont >= f:
            print(cont, end=' ', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')


""" O PARÂMETRO FLUSH SERVE PARA REMOVER O BUFFER DA FUNÇÃO SLEEP() DENTRO DA FUNÇÃO CONTADOR()  """

""" PROGRAMA PRINCIPAL """
contador(1, 10, 1)
contador(10, 0, 2)
print('=-' * 15)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = abs(int(input('Passo: ')))
if pas == 0:  # Caso o usuário digite 0, o passo será considerado 1
    pas = 1
contador(ini, fim, pas)
