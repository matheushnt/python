print('= =' * 10)
print(f'{'BOLETIM COM LISTAS COMPOSTAS':^30}')
print('= =' * 10)
ficha_estudantil = []
estudante = []
while True:
    estudante.append(str(input('Digite seu nome:\n')).strip())
    estudante.append(float(input('Primeira Nota: ')))
    estudante.append(float(input('Segunda Nota: ')))
    media = (estudante[1] + estudante[2]) / 2   # calcula a média de cada estudante
    estudante.append(media)
    ficha_estudantil.append(estudante[:])   # adiciona uma cópia da lista estudante na lista ficha_estudantil 
    estudante.clear()   # limpa o conteúdo da lista estudante
    resposta = str(input('Quer continuar? [S/N]\n')).strip()[0]
    while resposta not in 'SsNn':
        resposta = str(input('Quer continuar? [S/N]\n')).strip()[0]
    if resposta in 'Nn':
        break
print('=' * 42)
print(f'{'BOLETIM ESCOLAR':^42}')
print('=' * 42)
print(f'{'N°':<5} {'NOME':<15} {'MÉDIA':>20}')
print('-' * 42)
for indice, estudante in enumerate(ficha_estudantil):
    print(f'{indice:<5} {estudante[0]:<15} {estudante[3]:>20}')     # exibe o índice, o nome e a média de cada estudante registrado respectivamente
    print('-' * 42)
while True:
    notas = int(input('Mostrar notas de qual estudante? [999 para PARAR]: '))
    if notas == 999:
        break
    incr = 0    # verifica se o estudante foi registrado
    for nota, estudante in enumerate(ficha_estudantil):
        if notas == nota:   # verifica se o número digitado corresponde ao índice do estudante
            print(f'Notas de {estudante[0]} são: {ficha_estudantil[nota][1:3]}')    # exibe o nome e as notas do estudante
            incr += 1   # se a condição for atendida, é porque o estudante foi registrado
    if incr == 0:   # se não houver incrementos, é porque o estudante não foi registrado 
        print('Estudante não registrado.', end=' ')
