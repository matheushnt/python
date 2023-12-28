def aumentar(p, t):
    """
    -> Função que calculada uma taxa sobre o valor informado
    :param p: valor informado pelo usuário
    :return: retorna o valor calculado
    """
    calc = p + (p * (t / 100))
    return calc


def diminuir(p, t):
    """
    -> Função que diminue em 34% do valor informado
    :param p: valor informado pelo usuário
    :return: retorna o valor calculado
    """
    calc = p - (p * (t / 100))
    return calc


def metade(p):
    """
    -> Função que calcula metade do valor informado
    :param p: valor informado pelo usuário
    :return: retorna o valor calculado
    """
    calc = p / 2
    return calc


def dobro(p):
    """
    -> Função que calcula o dobro do valor informado
    :param p: valor informado pelo usuário
    :return: retorna o valor calculado
    """
    calc = p * 2
    return calc
