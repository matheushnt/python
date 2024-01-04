from lib.interface import *
from time import sleep

while True:
    resposta = menu(['Cadastrar Novo Usuário', 'Listar Usuários', 'Pesquisar Usuário', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho('Opção 1')
    elif resposta == 2:
        cabecalho('Opção 2')
    elif resposta == 3:
        cabecalho('Opção 3')
    elif resposta == 4:
        cabecalho('Saindo do programa... Até logo. 😉')
        break
    else:
        print('\033[0;31mERRO. Por favor, informar opção válida.\033[m')
    sleep(1.5)
