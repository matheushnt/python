""" ESCOPO DE VARIÁVEIS """


def teste():
    b = 10  # Variável de Escopo Local
    global c  # Variável de Escopo Global
    c = 50  # Alterando o valor da variável global (programa principal)
    print(f'Na função teste, b vale {b}')   # b existe apenas na função teste
    print(f'Na função teste, a vale {a}')   # a existe no programa principal, podendo ser acessada
    print(f'Na função teste, c vale {c}')


""" PROGRAMA PRINCIPAL """
a = 5   # Variável de Escopo Global
c = 15  # Variável de Escopo Global
print(f'No programa principal, a vale {a}')
teste()
print(f'No programa principal, c vale {c}')
print(f'No programa principal, b vale {b}')     # ERRO: b existe apenas dentro da função teste
