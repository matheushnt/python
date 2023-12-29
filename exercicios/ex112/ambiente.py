from exercicios.ex112.utilidades import dados as dds
from exercicios.ex112.utilidades.moeda import resumo
from exercicios.ex112.textos import titulo as ttl

ttl('entrada de dados monetários')
p = dds.ler_dinheiro('Digite o preço: R$ ')
resumo(p, 35, 29)
