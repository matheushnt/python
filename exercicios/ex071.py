print('=-' * 30)
print('{:^60}'.format('BANCO MATH'))
print('=-' * 30)
valor = int(input('Qual valor você quer sacar? \nR$ '))
montante = valor
nota50 = nota20 = nota10 = nota1 = 0    # contadores de cédulas
while montante >= 50:   # enquanto o montante for maior que a cédula vigente, retira 50 do montante
    montante -= 50
    nota50 += 1
while montante >= 20:   # enquanto o montante for maior que a cédula vigente, retira 20 do montante
    montante -= 20
    nota20 += 1
while montante >= 10:   # enquanto o montante for maior que a cédula vigente, retira 10 do montante
    montante -= 10
    nota10 += 1
while montante >= 1:    # enquanto o montante for maior que a cédula vigente, retira 1 do montante
    montante -= 1
    nota1 += 1
if nota50 > 0:
    print(f'Total de {nota50} cédulas de R$ 50,00.')
if nota20 > 0:
    print(f'Total de {nota20} cédulas de R$ 20,00.')
if nota10 > 0:
    print(f'Total de {nota10} cédulas de R$ 10,00.')
if nota1 > 0:
    print(f'Total de {nota1} cédulas de R$ 1,00.')
print('=-' * 30)
print('Volte sempre ao Banco Math. Tenha um bom dia!')
