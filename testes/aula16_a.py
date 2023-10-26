# variável composta TUPLA
lanche = ('hambúrguer', 'pizza', 'suco', 'sorvete')
print(lanche)
print(lanche[1])    # retorna o conteúdo referente ao índice
print(lanche[1:3])  # retorna o conteúdo referente a cada índice, EXCLUINDO O ÚLTIMO ELEMENTO
print(lanche[1:])   # retorna o conteúdo referente a cada índice até o final da tupla
print(lanche[:4])   # retorna o conteúdo referente a cada índice do início até o limite definido
print(lanche[:])    # retorna o conteúdo referente a cada índice sem saber o início e fim
print(lanche[-4])   # = 'hambúrguer'
print(lanche[-3])   # = 'pizza'
print(lanche[-2])   # = 'suco'
print(lanche[-1])   # = 'sorvete'
# TUPLAS SÃO IMUTÁVEIS
# lanche[1] = 'refrigerante'       = retornará um erro no terminal
