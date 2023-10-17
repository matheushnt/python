primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
contador = 1
while contador <= 10:
    print(f'{termo} ➞ 'if contador <= 10 else 'PAUSA', end=' ')
    termo += razao
    contador += 1
