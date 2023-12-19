""" DEFININDO AS FUNÇÕES DE CÁLCULOS ARITMÉTICOS """
def soma(a, b):     # definindo a função de soma passando cada parâmetro
    som = a + b
    print(f'A soma entre {a} e {b} é igual a {som}')
    print('-'*30)


def subtr(a, b):    # definindo a função de subtração passando cada parâmetro
    sub = a - b
    print(f'A subtração entre {a} e {b} é igual a {sub}')  
    print('-'*30) 


def mult(a, b):      # definindo a função de multiplicação passando cada parâmetro
    m = a * b
    print(f'A multiplicação entre {a} e {b} é igual a {m}')
    print('-'*30)


def div(a, b):       # definindo a função de divisão passando cada parâmetro
    d = a / b
    print(f'A divisão entre {a} e {b} é igual a {d}')
    print('-'*30)


""" PROGRAMA PRINCIPAL """
soma(10, 20)    # Chamando a função de soma passando o valor para cada parâmetro
subtr(7, 4)    # Chamando a função de subtração passando o valor para cada parâmetro
mult(225, 5)    # Chamando a função de multiplicação passando o valor para cada parâmetro
div(32, 16)    # Chamando a função de divisão passando o valor para cada parâmetro
