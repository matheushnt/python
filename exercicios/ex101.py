print('~' * 30)
print(f'{'SISTEMA DE VOTO':^30}')
print('~' * 30)


def voto(n):
    """
    -> Função que verifica a situação de voto de uma pessoa
    :param n: ano de nascimento
    :return: retorna a situação de voto da pessoa
    """
    from datetime import date

    # Obtém o ano atual do sistema
    ano_atual = date.today().year
    idade = ano_atual - n
    if idade < 16:
        return print(f'Com {idade} anos: VOTO NEGADO')
    elif 16 <= idade < 18:
        return print(f'Com {idade} anos: VOTO OPCIONAL')
    elif 18 <= idade < 65:
        return print(f'Com {idade} anos: VOTO OBRIGATÓRIO')
    elif idade >= 65:
        return print(f'Com {idade} anos: VOTO OPCIONAL')


nasc = int(input('Em que ano você nasceu?\n'))
voto(nasc)
