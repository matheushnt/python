from exercicios.ex115.lib.interface import cabecalho


def arq_existe(nome):
    try:
        txt = open(nome, 'rt')
        txt.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arq(nome):
    try:
        txt = open(nome, 'wt+')
        txt.close()
    except Exception as erro:
        print(f'Arquivo não criado. Motivo: {erro.__class__}')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def ler_arq(nome):
    try:
        txt = open(nome, 'rt')
    except Exception as erro:
        print(f'Não é possível ler arquivo. Motivo: {erro.__class__}')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        print(txt.read())
