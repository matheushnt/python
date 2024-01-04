def ler_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO. Por favor, informar opção válida.\033[m')
            continue
        except KeyboardInterrupt:
            print('o usuário preferiu não informar a opção')
            break
        else:
            return n


def linha(tam=42):
    """
    -> Função que cria uma linha horizontal para demarcação de cabeçalho.
    :param tam: Tamanho da linha.
    :return: Retorna a linha.
    """
    return print('-' * tam)


def cabecalho(txt):
    """
    -> Função para criar um cabeçalho.
    :param txt: Mensagem do Cabeçalho
    :return: sem retorno
    """
    linha()
    print(txt.center(42))
    linha()


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    linha()
    opc = ler_int('Sua opção: ')
    return opc
