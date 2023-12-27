def ajuda():
    """
    -> Função que explica o funcionamento de comandos do Pyhton
    :return: sem retorno
    """
    # Função de Pesonalização de Títulos
    def titulo(txt=''):
        tamln = len(txt) + 4
        print('-' * tamln)
        print(f'  {txt}')
        print('-' * tamln)

    # Função de Personalização de cores para Background
    def cores(cor):
        if cor == 'verde':
            print('\033[0;42m')
        elif cor == 'rosa':
            print('\033[0;45m')
        elif cor == 'vermelho':
            print('\033[0;41m')
        elif cor == 'preto':
            print('\033[0;40m')

    # Função para limpar as cores do Background de cada título
    def limpar():
        print('\033[m')

    from time import sleep
    # Loop principal
    while True:
        cores('verde')
        titulo('SISTEMA DE AJUDA PyHELP')
        limpar()
        cmd = str(input('Função ou Biblioteca: ')).lower().strip()
        if cmd == 'fim':
            cores('vermelho')
            titulo('ATÉ LOGO!')
            limpar()
            break
        else:
            cores('rosa')
            frase = 'Acessando o manual do comando ' + cmd
            titulo(frase)
            limpar()
            sleep(1)
            cores('preto')
            help(cmd)
            limpar()


# Programa principal
ajuda()
