def aumentar(p, t, form=False):
    """
    -> Função que calculada uma taxa sobre o valor informado
    :param p: valor informado pelo usuário
    :param t: taxa de aumento
    :param form: (Opcional) formatar ou não o valor
    :return: retorna o valor calculado
    """
    calc = p + (p * (t / 100))
    return calc if form is False else moeda(calc)


def diminuir(p, t, form=False):
    """
    -> Função que diminue em 34% do valor informado
    :param p: valor informado pelo usuário
    :param t: taxa de desconto
    :param form: (Opcional) formatar ou não o valor
    :return: retorna o valor calculado
    """
    calc = p - (p * (t / 100))
    return calc if form is False else moeda(calc)


def metade(p, form=False):
    """
    -> Função que calcula metade do valor informado
    :param p: valor informado pelo usuário
    :param form: (Opcional) formatar ou não o valor
    :return: retorna o valor calculado
    """
    calc = p / 2
    return calc if not form else moeda(calc)


def dobro(p, form=False):
    """
    -> Função que calcula o dobro do valor informado
    :param p: valor informado pelo usuário
    :param form: (Opcional) formatar ou não o valor
    :return: retorna o valor calculado
    """
    calc = p * 2
    return calc if not form else moeda(calc)


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
