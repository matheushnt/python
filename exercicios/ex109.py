# Importando apenas a função de título do Módulo Textos do Pacote Utilidades
from utilidades.textos import titulo
# Importando todas as funções do Módulo Moeda do Pacote Utilidades
from utilidades.moeda import *


titulo('escolhendo com formatação ou não')
num = float(input('Digite um preço: R$ '))
print(f'A metade de {num} é {moeda(metade(num), False)}')
print(f'O dobro de {num} é {moeda(dobro(num), True)}')
print(f'Aumentando em 27%, temos {moeda(aumentar(num), False)}')
print(f'Diminuindo em 34%, temos {moeda(diminuir(num), True)}')
