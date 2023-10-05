from datetime import date
print('\033[1;33;42m------ GRUPO DE MAIORIDADE ------\033[m')
menor = []      # lista vazia
maior = []      # lista vazia
anoAtual = date.today().year        # obtem o ano atual
for nome in range(1, 8):
    anoNasc = int(input('Digite seu Ano de Nascimento: '))
    grupoDeMaioridade = anoAtual - anoNasc          # calcula se a pessoa é menor ou maior de idade 
    if grupoDeMaioridade < 18:
        menor.append(anoNasc)       # se for menor de idade, vai ser adicionado na lista menor
    elif grupoDeMaioridade >= 18:
        maior.append(anoNasc)       # se for maior de idade, vai ser adicionado na lista maior
print(f'{len(menor)} pessoas são menores de idade.')        # confere o tamanho da lista menor
print(f'{len(maior)} pessoas são maiores de idade.')        # confere o tamanho da lista maior
print('\033[1;33;42m------ FIM ------\033[m')
