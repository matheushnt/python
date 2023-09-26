print('\033[0;34m=-=-=- CLASSIFICANDO ATLETAS -=-=-=\033[m')
from time import sleep
from datetime import date
anoDeNascimento = int(input('Informe seu ano de nascimento: '))
anoAtual = date.today().year        # obtem o ano atual de acordo com o Sistema Operacional
idade = anoAtual - anoDeNascimento
print('PROCESSANDO...')
sleep(2)
if idade <= 9:
    print(f'Você tem {idade} anos. Sua categoria é MIRIM.')
elif idade > 9 and idade <= 14:
    print(f'Você tem {idade} anos. Sua categoria é INFANTIL.')
elif idade > 14 and idade <= 19:
    print(f'Você tem {idade} anos. Sua categoria é JUNIOR.')
elif idade > 19 and idade <= 20:
    print(f'Você tem {idade} anos. Sua categoria é SÊNIOR.')
else:
    print(f'Você tem {idade} anos. Sua categoria é MASTER.')
print('\033[0;31m=-=-=- FIM -=-=-=\033[m')
