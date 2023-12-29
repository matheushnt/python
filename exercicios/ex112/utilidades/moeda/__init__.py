def aumentar(p, t, form=False):
    """
    -> Função que calculada uma taxa sobre o valor informado
    :param p: valor informado pelo usuário
    :param t: taxa de aumento
    :param form: (Opcional) formatar ou não o valor
    :return: retorna o valor calculado
    """
    calc = p + (p * (t / 100))
    return calc if form is False else moeda(int(calc))


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


def moeda(p=0):
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


def resumo(p, a, d):
    """
    -> Função que exibe um resumo sobre o valor informado pelo usuário
    :param p: valor a ser calculado
    :param a: porcentagem de aumento sobre o valor
    :param d: porcentagem de redução sobre o valor
    :return: sem retorno
    """
    # Cálculo de aumento
    aum = p + (p * (a / 100))
    # Cálculo de redução
    desc = p - (p * (d / 100))
    print('-'*45)
    print(f'{'RESUMO DO VALOR':^45}')
    print('-'*45)
    res = {'Preço Analisado': moeda(p),
           'Dobro do Preço': dobro(p, True),
           'Metade do Preço': metade(p, True),
           f'{a}% de Aumento': moeda(aum),
           f'{d}% de Redução': moeda(desc)}
    # Iteração sobre o Dicionário
    for k, v in res.items():
        print(f'{k:.<27} {v:<18}')
