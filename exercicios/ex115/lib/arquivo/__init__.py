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


# noinspection PyGlobalUndefined
def ler_arq(nome):
    # noinspection PyGlobalUndefined
    global file
    try:
        file = open(nome, 'rt')
    except Exception as erro:
        print(f'Não é possível ler arquivo. Motivo: {erro.__class__}')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        print(file.read())
    finally:
        file.close()


def cadastrar(arq, nm='<desconhecido>', idd=0):
    try:
        txt = open(arq, 'at')
    except Exception as erro:
        print(f'Não foi possível abrir o Arquivo. Motivo: {erro.__class__}')
    else:
        try:
            txt.write(f'{nm:.<30}{idd:>3} anos\n')
        except Exception as erro:
            print(f'Houve um ERRO no momento de inserir os dados. Motivo: {erro.__class__}')
        else:
            print(f'Novo registro de {nm} foi adicionado.')
            txt.close()
