from time import sleep
from datetime import date
print('--- Ano Bissexto ---')
print('Caso digite 0, será analisado o ano atual.')
ano = int(input('Digite um ano: '))
print('PROCESSANDO...')
if ano == 0:
    ano = date.today().year     # obtem a data atual, porém somente o ano nesse caso
sleep(2)
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:        # verifica se o ano é bissexto ou não
    print(f'{ano} é um ano bissexto.')
else:
    print(f'{ano} não é um ano bissexto.')
print('--- FIM ---')
# Para verificar se um ano é bissexto ou não, basta verificar os dois últimos algarismos e analisar se são múltiplos de 4, se sim, é um ano bissexto.
