from time import sleep
print('\033[0;34m=-=-=- CÁLCULO DA MÉDIA -=-=-=\033[m')
nota1 = float(input('Informe a sua primeira nota: '))
nota2 = float(input('Informe a sua segunda nota: '))
media = (nota1 + nota2) / 2     # calcula a média do estudante
print('CALCULANDO SUA MÉDIA...')
sleep(3)
if media < 5.0:
    print(f'Média: {media:.1f}. Você está REPROVADO.')
elif media >= 5.0 and media <= 6.9:
    print(f'Média: {media:.1f}. Você está de RECUPERAÇÃO')
elif media >= 7.0:
    print(f'Média: {media:.1f}. Você está APROVADO.')
print('\033[0;31m=-=-=- FIM -=-=-=\033[m')
