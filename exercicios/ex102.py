def fat(n, show=False):
    """
    -> Calcula o fatorial de um número
    :param n: número a ter o fatorial calculado
    :param show: (Opcional) mostrar o cálculo
    :return: retorna o fatorial calculado
    """
    f = 1   # Recebe os calculos após cada decremento
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c  # Calcula o fatorial a cada decremento
    return f


num = int(input('Número a ser calculado: '))
print(fat(num, show=True))
