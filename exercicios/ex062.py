primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
contador = 1
total = 0   # esse total será calculado ainda
mais = 10
while mais != 0:
    total += mais   # soma a quantidade de termos solicitados
    while contador <= total:
        print(f'{termo} ➞ ', end=' ')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?\n'))
print(f'Progressão finalizada com {total} termos.')
