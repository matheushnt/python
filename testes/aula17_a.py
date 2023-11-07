valores = [3, 6, 1, 9, 7, 2, 8, 4, 5]
print(type(valores))    # retorna o tipo da variável

""" ADICIONANDO VALORES """
valores[4] = 10     # substitue um valor por outro informando o índice
print(valores)
valores.append(15)  # adiciona o valor na última posição
print(valores)
valores.insert(6, 7)    # no índice 6 é adicionado o valor 7

""" ORGANIZANDO VALORES """
valores.sort(reverse=True)  # organiza de forma decrescente
print(valores)
valores.sort()      # organiza de forma crescente e alfabética
print(valores)

""" EXCLUINDO VALORES """
del valores[10]     # remove o conteúdo do índice 10
print(valores)
valores.pop()   # remove o último elemento
print(valores)
valores.pop(8)  # remove o conteúdo do índice 8
print(valores)
valores.remove(8)   # remove um elemento especificando o conteúdo
print(valores)

""" TAMANHO DA LISTA """
print(f'Essa lista possui {len(valores)} números')
