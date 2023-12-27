def aumentar(n):
    """
    -> Função que aumenta em 27% do valor informado
    :param n: valor informado pelo usuário
    :return: retorna o valor calculado
    """
    return n + (n * 0.27)


def diminuir(n):
    """
    -> Função que diminue em 34% do valor informado
    :param n: valor informado pelo usuário
    :return: retorna o valor calculado
    """
    return n - (n * 0.34)


def metade(n):
    """
    -> Função que calcula metade do valor informado
    :param n: valor informado pelo usuário
    :return: retorna o valor calculado
    """
    return n / 2


def dobro(n):
    """
    -> Função que calcula o dobro do valor informado
    :param n: valor informado pelo usuário
    :return: retorna o valor calculado
    """
    return n * 2


def moeda(n, form=False):
    """
    -> Função que formata para valor monetário brasileiro
    :param n: valor a ser formatado
    :param form: (Opcional) formata ou não o valor
    :return: retorna o valor com formato monetário brasileiro
    """
    if form:
        # Transforma o separador de milhar em _ (underline)
        n = f'{n:_.2f}'
        # Altera o separador de decimal por uma , (vírgula) e altera o separador de milhar por . (ponto)
        n = n.replace('.', ',').replace('_', '.')
        # Retorna o valor formatado
        return f'R$ {n}'
    else:
        # Retorna o valor sem formatação
        return n
