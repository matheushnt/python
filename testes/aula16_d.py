a = (1, 2, 3, 4, 5)
b = (6, 7, 8, 9, 10)
c = a + b
# as tuplas A e B se juntarão formando uma tupla maior
print(c)

d = (2, 4, 9, 5, 6)
e = (1, 3, 5, 10, 4)
f = d + e
print(f)
# o método interno .count() conta quantas vezes é exibido um caractere
print(f.count(5))
# o método interno .index() retorna o índice de um caractere
print(f.index(10))
# retorna o valor desejado a partir da posição que eu definir
print(f.index(5, 4))

# A TUPLA É IMUTÁVEL, PORÉM, É POSSÍVEL APAGAR ELA
pessoas = ('Matheus', 18, 'M', 'Gislane', 19, 'F')
del (pessoas)
