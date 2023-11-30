""" DECLARANDO UM DICIONÁRIO """
ficha = {'nome': 'Janaina',
         'idade': 50,
         'sexo': 'F',
         'filho(a)': 'Mauro'}
""" LAÇOS PARA PERCORRER O DICIONÁRIO """
for chave, valor in ficha.items():      # chave e valor recebem respectivamente seus dados
    print(f'{chave}: {valor}')
del ficha['filho(a)']   # excluindo um item do dicionário
print('= ='*10)
ficha['data de aniversário'] = '20/10/1980'     # adicionando um item no dicionário
for chave, valor in ficha.items():      # chave e valor recebem respectivamente seus dados
    print(f'{chave}: {valor}')
