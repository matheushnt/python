from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'lista_de_pessoas'
if not arq_existe(arq):
    criar_arq(arq)

while True:
    resposta = menu(['Cadastrar Nova Pessoa', 'Listar Pessoas', 'Pesquisar Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho('Opção 1')
    elif resposta == 2:
        ler_arq(arq)
    elif resposta == 3:
        cabecalho('Opção 3')
    elif resposta == 4:
        cabecalho('Saindo do programa... Até logo. 😉')
        break
    else:
        print('\033[0;31mERRO. Por favor, informar opção válida.\033[m')
    sleep(1.5)
