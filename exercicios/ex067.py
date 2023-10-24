cont = 1
while True:
    print('''    [ 0 ] Sair do programa
    [ 1 ] Somar
    [ 2 ] Subtrair
    [ 3 ] Multiplicar
    [ 4 ] Dividir''')
    print('-' * 50)
    opcao = int(input('Digite a opção que você queira realizar: '))
    
    if opcao == 0:
        print('Você saiu do programa.')
        break
    elif opcao == 1:
        num = int(input('Digite um número: '))
        if num < 0:
            print('Tabuada interrompida, pois foi solicitado um número negativo.')
            print('-' * 25)
            break
        while cont <= 10:
            print(f'{num} + {cont} = {num + cont}')
            cont += 1
            print('-' * 25)
    elif opcao == 2:
        num = int(input('Digite um número: '))
        if num < 0:
            print('Tabuada interrompida, pois foi solicitado um número negativo.')
            print('-' * 25)
            break
        while cont <= 10:
            print(f'{num} - {cont} = {num - cont}')
            cont += 1
            print('-' * 25)
    elif opcao == 3:
        num = int(input('Digite um número: '))
        if num < 0:
            print('Tabuada interrompida, pois foi solicitado um número negativo.')
            print('-' * 25)
            break
        while cont <= 10:
            print(f'{num} x {cont} = {num * cont}')
            cont += 1
            print('-' * 25)
    elif opcao == 4:
        num = int(input('Digite um número: '))
        if num < 0:
            print('Tabuada interrompida, pois foi solicitado um número negativo.')
            print('-' * 25)
            break
        while cont <= 10:
            print(f'{num} ÷ {cont} = {num / cont:.2f}')
            cont += 1
            print('-' * 25)
''' as opcões 2, 3, 4 estão com bugs, não estão executando corr retamente o cálculo '''
