lanche = ('hambúrguer', 'lasanha', 'pizza', 'pudim')
# descobrindo o tamanho da tupla
print(f'Eu comi {len(lanche)} comidas')

# Laço for iterando dentro da tupla da maneira antiga
for comida in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[comida]}')
print('Eu comi demais')

# Laço for iterando dentro da tupla da maneira nova
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Eu comi pra caramba')

# laço for retorna o índice e a informação desejada de uma maneira deselegante
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

# laço for retorna o índice e a informação desejada com o uso da função enumerate()
for posicao, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {posicao}')
