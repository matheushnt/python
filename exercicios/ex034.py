print('=== Aumento de Salário ===')
salario = float(input('Informe seu salário: R$ '))
if salario > 1250:
    aumento = (salario * 0.1) + salario
    print(f'Seu salário aumentará para R$ {aumento:.2f}')
if salario <= 1250:
    aumento = (salario * 0.15) + salario
    print(f'Seu salário aumentará para R$ {aumento:.2f}')
print('====== FIM ======')
