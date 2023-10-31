numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:     # laço infinito para verificar a resposta do usuário
    while True:     # laço infinito
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:  # se a condição for atendida, o laço é interrompido (VALIDAÇÃO)
            break
        print('Tente novamente. ', end='')
    print(f'Você digitou {numeros[num]}')   # numeros é a tupla, o valor digitado pelo usuário será o índice
    resp = str(input('Você quer continuar?\n')).strip()[0]
    while resp not in 'SsNn':
        resp = str(input('Você quer continuar?\n')).strip()[0]
    print('-' * 40)
    if resp in 'Ss':    # se a resposta for sim, repete o bloco
        while True:  # laço infinito
            num = int(input('Digite um número entre 0 e 20: '))
            if 0 <= num <= 20:  # se a condição for atendida, o laço é interrompido (VALIDAÇÃO)
                break
            print('Tente novamente. ', end='')
        print(f'Você digitou {numeros[num]}')  # numeros é a tupla, o valor digitado pelo usuário será o índice
        resp = str(input('Você quer continuar?\n')).strip()[0]
        while resp not in 'SsNn':
            resp = str(input('Você quer continuar?\n')).strip()[0]
        print('-' * 40)
        if resp not in 'Ss':    # se a resposta for diferente de não, interrompe o laço
            print('Fim da execução')
            break
    else:
        print('Fim da execução')
        break
