numeros = []
while True:
    num = int(input('Digite um número: '))
    if num in numeros:
        num = int(input('Número já informado. Digite outro: '))
        while num in numeros:
            num = int(input('Número já informado. Digite outro: '))
    else:
        numeros.append(num)
    resp = str(input('Quer continuar? [S/N]\n'))[0].strip()
    if resp in 'Nn':
        break
print(f'Os números informados foram: {num}', end=' ')
num_organizados = sorted(numeros)
for n in num_organizados:
    print(f'{n}', end=' ')
