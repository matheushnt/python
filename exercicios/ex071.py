print('=-' * 30)
print('{:^60}'.format('BANCO MATH'))
print('=-' * 30)
valor = int(input('Qual valor você quer sacar? \nR$ '))
montante = valor
cedula = 50
cedulas = 0
while True:
    if montante >= cedula:
        montante -= cedula
        cedulas += 1
    else:
        if cedulas > 0:
            print(f'Total de {cedulas} cédulas de R$ {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        cedulas = 0
        if cedulas == 0:
            break
print('=-' * 30)
print('Volte sempre ao Banco Math. Tenha um bom dia!')
