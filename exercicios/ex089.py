ficha_estudantil = []
estudante = []
while True:
    estudante.append(str(input('Digite seu nome:\n')).strip())
    estudante.append(float(input('Primeira Nota: ')))
    estudante.append(float(input('Segunda Nota: ')))
    media = (estudante[1] + estudante[2]) / 2
    estudante.append(media)
    ficha_estudantil.append(estudante[:])
    estudante.clear()
    resposta = str(input('Quer continuar? [S/N]\n')).strip()[0]
    while resposta not in 'SsNn':
        resposta = str(input('Quer continuar? [S/N]\n')).strip()[0]
    if resposta in 'Nn':
        break
print(' -' * 15)
print(f'{'BOLETIM ESCOLAR':^30}')
print(' -' * 15)
print(f'{'N°':<5} {'NOME':<10} {'MÉDIA':>15}')

for indice, estudante in enumerate(ficha_estudantil):
    print(f'{indice:<5} {estudante[0]:<10} {estudante[3]:>15}')
print('--' * 15)
while True:
    notas = int(input('Mostrar notas de qual estudante? [999 para PARAR]: '))
    if notas == 999:
        break
    for nota, estudante in enumerate(ficha_estudantil):     # foi encontrado um problema no FOR
        if notas == nota:
            print(f'Notas de {estudante[0]} são:', end=' ')
            for estudante in ficha_estudantil:
                print(f'{estudante[1:3][nota]}', end=' ')   # meu problema está aqui
    print('\nEstudante não registrado.', end=' ')       
