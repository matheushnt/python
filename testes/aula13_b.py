from time import sleep
num = int(input('Digite um numero: '))
for contador in range(1, num+1):     # a repeticao vai de 1 ate numero digitado pelo usuario e no final da execucao sera somado mais 1
    print(contador)
    sleep(0.2)

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
incremento = int(input('Passo: '))
for contador in range(inicio, fim+1, incremento):
    print(contador)
    sleep(0.2)
print('FIM')
