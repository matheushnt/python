print('--- Ano Bissexto ---')
ano = int(input('Digite um ano: '))
if ano % 4 == 0:        # verifica se o ano é bissexto ou não
    print(f'{ano} é um ano bissexto.')
else:
    print(f'{ano} não é um ano bissexto.')
print('--- FIM ---')
# Para verificar se um ano é bissexto ou não, basta verificar os dois últimos algarismos e analisar se são múltiplos de 4, se sim, é um ano bissexto.
