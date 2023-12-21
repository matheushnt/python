""" FATORIAL """


def fat(n=1):
    """
    -> Calcula o fatorial de um número.
    :param n: número a ser calculado o fatorial
    :return: retorna o fatorial do número calculado
    """
    f = 1   # Recebe a multiplicação entre os valores após iteração do laço
    for c in range(n, 1, -1):
        f *= c
    return f


num = int(input('Fatorial de: '))
resp = fat(num)
print(f'O fatorial de {num} é igual a {resp}')
