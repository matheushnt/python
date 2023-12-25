print('-'*30)
print(f'{'ENTRADA E VALIDAÇÃO DE DADOS':^30}')
print('-'*30)


def lnum(msg):  # parâmetro formal
    """
    -> Função que lê e valida a entrada de dados
    :param msg: mensagem da função lnum()
    :return: retorna um valor numérico
    """
    cond = False
    valor = 0
    while True:
        global num
        # Input que solicita dados do usuário
        num = input(msg)
        # Condição para verificar se os dados informados são numéricos
        if num.isnumeric():
            # Caso seja, o valor é tranformado para inteiro
            valor = int(num)
            # A Condição se torna VERDADE e o laço se encerrará
            cond = True
        # Caso os dados informados não sejam numéricos, o laço se repete
        else:
            print("\033[0;031mERRO! Digite um número inteiro válido.\033[m")
        # Se a condição for VERDADE, o laço é interrompido
        if cond:
            break
    return valor


num = lnum('Digite um número: ')    # Chamada da função passando o parâmetro real
print(f'Você acabou de digitar o número {num}')
