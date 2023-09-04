salario = float(input('Informe seu salário: '))     # lê a entrada de dados
aumento = salario + (salario * 0.15)    # calcula o aumento do salário
salNovo = abs(aumento - salario)    # calcula de quanto será esse aumento
print(f'Seu salário terá um aumento de R$ {salNovo:.2f}')   # exibe a respostas
print(f'Com esse acréscimo de 15%, seu novo salário será: R$ {aumento:.2f}')    # exibe a respostas