produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
            'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-' * 60)
print(f'{'LISTAGEM DE PREÇOS':^60}')
print('-' * 60)
for posicao in range(0, len(produtos)):
    if posicao % 2 == 0:
        print(f'{produtos[posicao]:.<50}', end='')
    else:
        print(f'R$ {produtos[posicao]:>6.2f}')
print('=' * 60)
