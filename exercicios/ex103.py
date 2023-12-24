def ficha(n='', g=''):
    """
    -> Função que exibe a ficha de um jogador
    :param n: nome do jogador
    :param g: quantidade de gols do jogador
    :return: sem retorno
    """
    print('-'*30)
    if n == '':
        n = '<desconhecido>'
    if g == '':
        g = '0'
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


nome = str(input('Nome do Jogador: ')).capitalize()
gols = str(input('Número de Gols: '))
ficha(nome, gols)
