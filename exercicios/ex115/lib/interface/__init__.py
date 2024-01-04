def linha(tam=42):
    """
    -> Função que cria uma linha horizontal para demarcação de cabeçalho.
    :param tam: Tamanho da linha.
    :return: Retorna a linha.
    """
    return '-' * tam


def cabecalho(txt):
    """
    -> Função para criar um cabeçalho.
    :param txt: Mensagem do Cabeçalho
    :return: sem retorno
    """
    linha()
    print(txt.center())
    linha()
