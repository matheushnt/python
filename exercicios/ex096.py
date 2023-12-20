def titulo(txt):    # Função de título personalizado
    print('-'*30)
    print(txt)
    print('-'*30)


def area(c, l): # Função de cálculo de área
    a = c * l
    print('-'*30)
    print(f'A área de um terreno de {c}x{l} é de {a}m²')    


""" PROGRAMA PRINCIPAL """
titulo(f'{'CÁLCULO DE ÁREA':^30}')  # Chamando a função 
compr = float(input('Comprimento do terreno (m): '))
larg = float(input('Largura do terreno (m): '))
area(compr, larg)  # Chamando a função
