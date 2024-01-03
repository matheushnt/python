def ler_int():
    """
    -> Função que valida Números Inteiros.
    :return: retorna o Número Inteiro digitado.
    """
    # É feita várias tentativas até o usuário informar um Número Inteiro
    while True:
        # Tentativa de obter um Número Inteiro
        try:
            num = int(input('Digite um Número Inteiro: '))

        # Caso o usuário informe números não inteiros, dispara uma Exceção
        except (ValueError, TypeError):
            print('\033[0;31mERRO: os dados informados são inválidos.\033[m')
            # Interrompe o laço e pula para próxima iteração
            continue

        # Caso o usuário não digite valores, dispara uma Exceção
        except KeyboardInterrupt:
            print('O usuário preferiu não informar valores.')
            break

        # Caso usuário digite o valor esperado, o programa é encerrado com êxito
        else:
            return print(f'Você digitou o Número Inteiro: {num}')


def ler_float():
    """
    -> Função que valida Números Reais.
    :return: retorna o Número Real digitado.
    """
    # É feita várias tentativas até o usuário informar um Número Real
    while True:
        # Tentativa de obter um Número Inteiro
        try:
            num = float(input('Digite um Número Real: '))

        # Caso o usuário informe números não reais, dispara uma Exceção
        except (ValueError, TypeError):
            print('\033[0;31mERRO: os dados informados são inválidos.\033[m')
            # Interrompe o laço e pula para próxima iteração
            continue

        # Caso o usuário não digite valores, dispara uma Exceção
        except KeyboardInterrupt:
            print('O usuário preferiu não informar valores.')
            break

        # Caso usuário digite o valor esperado, o programa é encerrado com êxito
        else:
            return print(f'Você digitou o Número Real: {num:.2f}')


# Programa principal
ler_int()
ler_float()
