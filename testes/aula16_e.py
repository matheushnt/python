pessoas = ('Matheus', 'Gislane', 'Fabinho', 'Neto')
idades = (18, 19, 13, 26)
# o método zip() agrupa elementos de diferentes tuplas
for indivíduos in zip(pessoas, idades):
    print(f'{indivíduos}')
