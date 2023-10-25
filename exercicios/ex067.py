while True:     # o laço será infinito enquanto a opção digitada pelo usuário for diferente de zero
    cont = 1
    print('''    [ 0 ] Sair do programa
    [ 1 ] Somar
    [ 2 ] Subtrair
    [ 3 ] Multiplicar
    [ 4 ] Dividir''')
    print('-' * 50)
    # variável recebe um novo digito de opção a cada nova iteração
    opcao = int(input('Digite a opção que você queira realizar: '))

    # interrompe o laço caso opcao seja 0
    if opcao == 0:
        print('Você saiu do programa.')
        break

    # laço para o cálculo de adição
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

    # laço para o cálculo de subtração
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

    # laço para o cálculo de multiplicação
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

    # laço para o cálculo de divisão
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
