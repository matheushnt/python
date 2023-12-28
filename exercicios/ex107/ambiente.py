# Importando apenas a função de título do Módulo Textos
from textos import titulo
# Importando todas as funções do Módulo Moeda
from moeda import *


titulo('módulo moeda em python')
num = float(input('Digite um preço: R$ '))
aum = float(input('Taxa de Aumento [%]: '))
desc = float(input('Taxa de Redução [%]: '))
print(f'A metade de {num} é {metade(num)}')
print(f'O dobro de {num} é {dobro(num)}')
print(f'Aumentando em {aum}%, temos {aumentar(num, aum)} ')
print(f'Diminuindo em {desc}%, temos {diminuir(num, desc)}')
