from time import sleep
print('\033[1;35m---=---=---= MENU DE OPÇÕES =---=---=---\033[m')
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0   # inicia o laço
while opcao != 5:   # itera o laço enquanto a opção for diferente de cinco
    # apresenta o menu a cada iteração
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos valores
    [ 5 ] sair do programa''')
    opcao = int(input('»»» Qual a sua opção?\n'))   # recebe a opção
    print('PROCESSANDO...')
    sleep(1)
    if opcao == 1:
        print(f'A soma entre {n1} e {n2} é igual a {n1 + n2}')
        print('=-=' * 20)
    elif opcao == 2:
        print(f'A multiplicação entre {n1} e {n2} é igual a {n1 * n2}')
        print('=-=' * 20)
    elif opcao == 3:
        maior = n1
        if n2 > n1:
            maior = n2
        print(f'O maior número digitado foi {maior}')
        print('=-=' * 20)
    elif opcao == 4:
        print('Informe novamente os números')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print('=-=' * 20)
    elif opcao == 5:    # finaliza o laço pois deixa de satisfazer a condição
        print('FINALIZANDO...')
        sleep(1)
    else:
        print('Opção inválida. Tente novamente.')
print('\033[1;31m---=---=---= FIM =---=---=---\033[m')
