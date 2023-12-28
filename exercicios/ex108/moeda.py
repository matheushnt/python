def aumentar(p, t):
    """
    -> Função que calculada uma taxa sobre o valor informado
    :param p: valor informado pelo usuário
    :param t: taxa de aumento
    :return: retorna o valor calculado
    """
    calc = p + (p * (t / 100))
    return calc


def diminuir(p, t):
    """
    -> Função que diminue em 34% do valor informado
    :param p: valor informado pelo usuário
    :param t: taxa de desconto
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


def moeda(p):
    """
    -> Função que formata para valor monetário brasileiro
    :param p: valor a ser formatado
    :return: retorna o valor com formato monetário brasileiro
    """
    # Transforma o separador de milhar em _ (underline)
    p = f'{p:_.2f}'
    # Altera o separador de decimal por uma , (vírgula) e altera o separador de milhar por . (ponto)
    p = p.replace('.', ',').replace('_', '.')
    # Retorna o valor formatado
    return f'R$ {p}'
