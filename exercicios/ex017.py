from math import hypot      # importando somente o método hypot()
co = float(input('Informe o comprimento do Cateto Oposto: '))
ca = float(input('Informe o comprimento do Cateto Adjacente: '))
hip = hypot(co, ca)     # o método hypot realiza o cálculo do comprimento da hipotenusa
print(f'O comprimento da Hipotenusa mede: {hip:.3f} ')
# hip = (co ** 2) + (ca ** 2) ** 1/2
