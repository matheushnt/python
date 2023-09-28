print('\033[1;31m--*-*-- ÍNDICE DE MASSA CORPORAL --*-*--\033[m')
from time import sleep
peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
print('PROCESSANDO...')
sleep(2)
imc = peso / (altura ** 2)      # calcula o IMC da pessoa
if imc < 18.5:
    print(f'Seu IMC é: {imc:.1f}')
    print('Abaixo do Peso.')
elif imc <= 25:
    print(f'Seu IMC é: {imc:.1f}')
    print('Peso ideal.')
elif imc <= 30:
    print(f'Seu IMC é: {imc:.1f}')
    print('Sobrepeso.')
elif imc <= 40:
    print(f'Seu IMC é: {imc:.1f}')
    print('Obesidade.')
else:
    print(f'Seu IMC é: {imc:.1f}')
    print('Obesidade Mórbida.')
print('\033[1;36m--*-*-- FIM --*-*--\033[m')
