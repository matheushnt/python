def titulo(msg):
    """
    -> Função que cria um título personalizado
    :param msg: recebe o a frase para Título
    :return: sem retorno
    """
    tamln = len(msg) + 4
    print('='*tamln)
    print(f'  {msg.upper()}')
    print('='*tamln)
