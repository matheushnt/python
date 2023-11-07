""" CONECTANDO LISTAS """
a = [3, 7, 4, 9]
b = a
b[1] = 4
# No Python, ele conecta duas listas caso uma seja atribuida por outra
c = [1, 0, 4, 6]
d = c[:]    # a lista D está recebendo uma cópia de C
d[1] = 2
print(f'Lista : {c}')
print(f'Lista B: {d}')
