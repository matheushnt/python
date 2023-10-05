from statistics import mean
idades = []
nomes = []
for pessoa in range(1, 3):
    nome = str(input('Qual o seu nome?\n'))
    nomes.append(nome)
    idade = int(input('Qual sua idade?\n'))
    idades.append(idade)
    sexo = str(input('Qual seu sexo?\n')).lower().strip()
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
mediaDeIdade = mean(idades)     # o método mean() calcula a média aritmética de uma lista de números
maiorIdade = max(idades)        # obtém o maior valor da lista idades
homemMaisVelho = idades.index(maiorIdade)       # obtém o INDEX do maior valor da lista idades
print(f'A média da idades dos indivíduos é igual a {mediaDeIdade:.2f}')
print(f'{nomes[homemMaisVelho]} é a pessoa mais velha com {maiorIdade} anos')
