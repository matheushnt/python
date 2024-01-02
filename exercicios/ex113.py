def ler_int(msg):
    """
    -> Função para validar números inteiros
    :param msg: mensagem para a função input()
    :return: sem retorno
    """
    # Tentativa de obter um número inteiro
    try:
        num = int(input(msg))

    # Dispara a Exceção caso o usuário interrompa a execução do programa
    except KeyboardInterrupt:
        print('Dados não foram inseridos')

    # Dispara a Exceção caso os dados sejam de tipagem diferente do pedido
    except (ValueError, TypeError):
        print('O valor informado é inválido')

        # É realizado várias tentativas até o usuário informar um valor válido
        while True:
            try:
                """ BREVE VALIDAÇÃO DE DADOS """
                cond = False
                num = str(input(msg))
                if num.isnumeric():
                    cond = True
                    num = int(num)
                else:
                    print('O valor informado é inválido')
                if cond:
                    print(f'Você digitou o número inteiro {num}')
                    break

            # Dispara a Exceção caso o usuário interrompa a execução do programa
            except KeyboardInterrupt:
                print('Dados não foram inseridos')
                # Interrompe o laço
                break
    else:
        print(f'Você digitou o número inteiro {num}')


def ler_float(msg):
    """
    -> Função para validar números decimais
    :param msg: mensagem para a função input()
    :return: sem retorno
    """
    # Tentativa de obter um número inteiro
    try:
        num = float(input(msg))

    # Dispara a Exceção caso o usuário interrompa a execução do programa
    except KeyboardInterrupt:
        print('Dados não foram inseridos')

    # Dispara a Exceção caso os dados sejam de tipagem diferente do pedido
    except (ValueError, TypeError):
        print('O valor informado é inválido')

        # É realizado várias tentativas até o usuário informar um valor válido
        while True:
            try:
                """ BREVE VALIDAÇÃO DE DADOS """
                cond = False
                num = str(input(msg))
                if num.isnumeric():
                    cond = True
                    num = float(num)
                else:
                    print('O valor informado é inválido')
                if cond:
                    print(f'Você digitou o número decimal {num:.2f}')
                    break

            # Dispara a Exceção caso o usuário interrompa a execução do programa
            except KeyboardInterrupt:
                print('Dados não foram informados')
                # Interrompe o laço
                break
    else:
        print(f'Você digitou o número decimal {num:.2f}')


# Programa principal
ler_int('Digite um Inteiro: ')
ler_float('Digite um Decimal: ')
