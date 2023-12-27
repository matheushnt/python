# Importando apenas a função de título do Módulo Textos do Pacote Utilidades
from utilidades.textos import titulo
# Importando todas as funções do Módulo Moeda do Pacote Utilidades
from utilidades.moeda import *


titulo('módulo moeda em python')
num = float(input('Digite um preço: R$ '))
print(f'A metade de {num} é {metade(num)}')
print(f'O dobro de {num} é {dobro(num)}')
print(f'Aumentando em 27%, temos {aumentar(num)} ')
print(f'Diminuindo em 34%, temos {diminuir(num)}')
