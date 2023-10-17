print('\033[1;34m******** GERADOR DE PA ********\033[m')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro    # armazena o primeiro termo
contador = 1    # conta a quantidade de termos
while contador <= 10:
    print(f'{termo}', end=' ')
    print('➞' if contador < 10 else '', end=' ')
    termo += razao  # soma termo com a razão
    contador += 1   # conta os termos
print('\033[1;33m******** FIM ********\033[m')
