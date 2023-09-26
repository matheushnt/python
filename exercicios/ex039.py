print('\033[0;32m****** ALISTAMENTO MILITAR ******\033[m')
from time import sleep
from datetime import date
anoAtual = date.today().year        # obtem o ano atual de acordo com o Sistema Operacional
dataDeNascimento = int(input('Informe o seu ano de nascimento: '))
idade = anoAtual - dataDeNascimento
alistamento = 18
print('PROCESSANDO...')
sleep(2)
if idade < alistamento: 
    tempoRestante = idade - alistamento
    print(f'Você ainda tem {idade} anos. Faltam {abs(tempoRestante)} anos para você se alistar. Aguarde até completar 18 anos para comparecer a uma Junta Militar para realizar seu Alistamento Militar.')
elif idade == alistamento:
    print(f'Você tem {idade} anos. Compareça a Junta Militar mais próxima de você para realizar seu Alistamento Militar.')
else:
    tempoAtrasado = idade - alistamento
    print(f'Você tem {idade} anos. Deveria ter se apresentado há {tempoAtrasado} anos. Compareça o mais rápido possível a uma Junta Militar para realizar seu Alistamento Militar.')
print('\033[0;36m****** FIM ******\033[m')
