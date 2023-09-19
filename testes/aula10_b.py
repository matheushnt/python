n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print(f'Sua média é: {media:.1f}')
print(f'PARABÉNS' if media>=7 else 'REPROVADO')     # condição simplificada

"""
if media >= 7:
    print('APROVADO')
else:
    print('REPROVADO')
"""
# no Python, blocos de códigos são identificados através da indentação dos comandos
