from time import sleep
print('\033[1;33m=-=-=- TABUADA 2.0 -=-=-=\033[m')
operacoes = int(input('Digite 1 para Adição\nDigite 2 para Subtração\nDigite 3 para Divisão\nDigite 4 para Multiplicação.\n'))
if operacoes == 1:      # soma
    num = int(input('Número: '))        
    for contador in range(1, 11):
        soma = num + contador
        print(f'{num} + {contador} = {soma:.1f}')
        sleep(0.03)
elif operacoes == 2:    # subtração     
    num = int(input('Número: '))
    for contador in range(1, 11):
        subtracao = num - contador
        print(f'{num} - {contador} = {subtracao:.1f}')
        sleep(0.03)
elif operacoes == 3:    # divisão
    num = int(input('Número: '))
    for contador in range(1, 11):
        divisao = num / contador
        print(f'{num} ÷ {contador} = {divisao:.1f}')
        sleep(0.03)
elif operacoes == 4:    # multiplicação
    num = int(input('Número: '))
    for contador in range(1, 11):
        multiplicacao = num * contador
        print(f'{num} x {contador} = {multiplicacao:.1f}')
        sleep(0.03)
else:
    print('Número inválido.')
print('\033[1;32m=-=-=- FIM -=-=-=\033[m')
