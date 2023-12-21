""" RETORNO DE FUNÇÕES """


def soma(a=0, b=0, c=0):
    s = a + b + c
    return s    # Retorna o valor calculado para a chamada da função


# Programa principal
# Valor retornado a chamada é atribuido a uma variável
r1 = soma(5, 2, 8)
r2 = soma(9, 4, 7)
r3 = soma(2, 1)
r4 = soma(2)
print(f'Os cálculos deram {r1}, {r2}, {r3}, {r4}')
# valor retornado a chamada é exibido na tela sem atribuição a uma variável
print(f'Valor calculado: {soma(100, 100)}')
