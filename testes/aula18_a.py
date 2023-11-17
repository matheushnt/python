teste = list()  # lista vazia
teste.append('Matheus')     # adicionando conteúdo
teste.append(18)    # adicionando conteúdo
galera = list() # lista vazia
galera.append(teste[:])    # adicionando uma cópia da lista teste dentro da lista galera
teste[0] = 'Gislane'    # alterando o conteúdo da lista teste
teste[1] = 19   # alterando o conteúdo da lista teste
galera.append(teste[:]) # adicionando uma cópia da lista teste alterada dentro da lista galera
print(galera)
