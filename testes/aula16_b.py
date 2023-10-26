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
