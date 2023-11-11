expressao = str(input('Digite uma expressão: '))    # entrada da expressão
contador_parenteses = 0     # variável que irá contar a quantidade de parênteses
for parenteses in expressao:    # laço irá percorrer cada caractere da expressão
    if parenteses == '(':
        contador_parenteses += 1    # caso encontre uma parêntese aberto, será incrementado a váriavel contador_parenteses
    elif parenteses == ')':
        contador_parenteses -= 1    # caso encontre uma parêntese fechado, será decrementado a váriavel contador_parenteses
    if contador_parenteses < 0:     # caso a variável contador_parenteses seja um valor negativo, será interrompido o laço
        break   # interrompe o laço
if contador_parenteses == 0:
    print('Expressão válida')   # se o contador_parenteses for igual a zero, a expressão será válida
else:
    print('Expressão inválida') # se o contador_parenteses for positivo ou negativo, a expressão será inválida
