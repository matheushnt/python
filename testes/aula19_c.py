""" DECLARANDO UM DICIONÁRIO """
pessoa = {'nome': 'Antônio',
          'idade': 30,
          'sexo': 'M'}
""" LAÇO PARA PERCORRER O DICIONÁRIO """
for chave, valor in pessoa.items():     # chave e valor recebem respectivamente seus dados
    print(f'{chave} = {valor}')
    