""" DOCSTRINGS """


def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Matheus durante os estudos de Python.
    """
    c = i
    while c <= f:
        print(c, end=' ')
        c += p
    print('FIM!')


contador(1, 10, 1)
help(contador)  # Exibe a Docstring da função contador()
