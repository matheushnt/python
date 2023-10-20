numeros = []
soma = 0
num = int(input('Digite um número: '))
numeros.append(num)
resp = str(input('Quer continuar? [SIM/NÃO]: ')).strip()
if resp in 'SIMsim':
    while resp in 'SIMsim':
        num = int(input('Digite um número: '))
        soma += num
        numeros.append(num)
        resp = str(input('Quer continuar? [SIM/NÃO]: ')).strip()

''' Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores. '''
