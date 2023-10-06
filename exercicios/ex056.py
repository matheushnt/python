from statistics import mean
from time import sleep
print('\033[1;30;107m------ ANALISADOR ------\033[m')
idades = []
nomes = []
for pessoa in range(1, 4):
    nome = str(input('Qual o seu nome?\n').capitalize())
    nomes.append(nome)      # adiciona o nome digitado dentro da lista nomes
    idade = int(input('Qual sua idade?\n'))
    idades.append(idade)    # adiciona a idade digitada dentro da lista idades
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
mediaDeIdade = mean(idades)     # o método mean() calcula a média aritmética de uma lista de números
maiorIdade = max(idades)        # obtém o maior valor da lista idades
pessoaMaisVelha = idades.index(maiorIdade)       # obtém o ÍNDICE da maior idade da lista idades
sleep(1)
print(f'A média da idades dos indivíduos é igual a {mediaDeIdade:.2f}')
print(f'{nomes[pessoaMaisVelha]} é a pessoa mais velha com {maiorIdade} anos')
print('\033[1;30;107m------ FIM ------\033[m')
