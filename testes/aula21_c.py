""" PARÂMETROS OPCIONAIS """


def soma(a=0, b=0, c=0):
    """ Ao igualar a 0 cada parâmetro, são considerados opcionais, não retornando nenhum problema
    caso não sejam atribuido valores nos parâmetros reais
    """
    s = a + b + c
    print(s)


soma(3, 7)
soma(c=3, a=10, b=2)    # Informando cada parâmetro real fora de forma desordenada
