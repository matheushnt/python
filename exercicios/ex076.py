produtos_precos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
                   'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
                   'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-' * 60)
print(f'{'LISTAGEM DE PREÇOS':^60}')
print('-' * 60)
for produtos in range(0, len(produtos_precos), 2):
    print(f'{produtos_precos[produtos]}')
for precos in range(1, len(produtos_precos), 2):
    print(f'{produtos_precos[precos]}')
