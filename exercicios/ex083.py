expressao = str(input('Digite uma expressão: '))
contador_parenteses = 0
for parenteses in expressao:
    if parenteses == '(':
        contador_parenteses += 1
    elif parenteses == ')':
        contador_parenteses -= 1
    if contador_parenteses < 0:
        break
if contador_parenteses == 0:
    print('Expressão válida')
else:
    print('Expressão inválida')
TODO: explicar o passo a passo
