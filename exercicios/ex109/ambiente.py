# Importando apenas a função de título do Módulo Textos
from textos import titulo
# Importando todas as funções do Módulo Moeda
from moeda import *


titulo('módulo moeda em python')
num = float(input('Digite um preço: R$ '))
aum = float(input('Taxa de Aumento [%]: '))
desc = float(input('Taxa de Redução [%]: '))
print(f'A metade de {moeda(num)} é {metade(num, True)}')
print(f'O dobro de {moeda(num)} é {dobro(num, True)}')
print(f'Aumentando em {aum}%, temos {aumentar(num, aum, True)} ')
print(f'Diminuindo em {desc}%, temos {diminuir(num, desc, True)}')
