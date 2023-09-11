from math import hypot
co = float(input('Informe o comprimento do Cateto Oposto: '))
ca = float(input('Informe o comprimento do Cateto Adjacente: '))
hip = hypot(co, ca)
print(f'O comprimento da Hipotenusa mede: {hip:.3f} ')