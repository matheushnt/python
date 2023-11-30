""" ADICIONANDO DICIONÁRIOS DENTRO DE UMA LISTA """
brasil = []
# declarando dicionários
estado1 = {'uf': 'Amapá',
           'sigla': 'AP'}
estado2 = {'uf': 'Pará',
           'sigla': 'PA'}
estado3 = {'uf': 'Ceará',
           'sigla': 'CE'}
""" ADICIONANDO CADA DICIONÁRIO DENTRO DA LISTA """
brasil.append(estado1)
brasil.append(estado2)
brasil.append(estado3)
print(brasil)   # retorna o conteúdo da lista, ou seja, os dicionários
print('= ='*10)
print(brasil[0])    # {'uf': 'Amapá', 'sigla': 'AP}
print(brasil[1])    # {'uf': 'Pará', 'sigla': 'PA'}
print(brasil[2])    # {'uf': 'Ceará', 'sigla': 'CE'}
print('= ='*10)
print(brasil[0]['sigla'])   # AP
print(brasil[1]['uf'])      # Pará
print(brasil[2]['uf'])      # Ceará
