from time import sleep
print('\033[0;33m=-=-=- ANALISANDO TRIÂNGULOS -=-=-=\033[m')
seg1 = float(input('Informe o comprimento do primeiro segmento: '))
seg2 = float(input('Informe o comprimento do segundo segmento: '))
seg3 = float(input('Informe o comprimento do terceiro segmento: '))
print('PROCESSANDO...')
sleep(2)
if (seg1 + seg2 > seg3) and (seg1 + seg3 > seg2) and (seg3 + seg2 > seg1):      # verifica se é possível criar um triângulo
    print('De acordo com os segmentos informados, é possível criar um Triângulo.')
    if (seg1 == seg2) and (seg1 == seg3):       # todos os segmentos tem que ser iguais
        print('Com os segmentos informados, será formado um Triângulo Equilátero.')
    elif (seg1 == seg2) or (seg1 == seg3) or (seg3 == seg2):        # dois segmentos tem que ser iguais
        print('Com os segmentos informados, será formado um Triângulo Isósceles.')
    else:       # todos os segmentos tem que ser diferentes
        print('Com os segmentos informados, será formado um Triângulo Escaleno.')
    opcao = int(input('Digite 1 caso queira saber o Perímetro do Triângulo. Digite 2 caso queira saber a Área do Triângulo: '))
    if opcao == 1:
        perimetro = seg1 + seg2 + seg3      # calcula o perímetro
        print(f'O Perímetro do Triângulo mede {perimetro}')
    elif opcao == 2:
        base = float(input('Informe o maior lado do Triângulo: '))
        altura = float(input('Informe a altura do Triângulo: '))
        formula = (base * altura) / 2       # calcula a área
        print(f'A Área do Triângulo mede {formula} cm.')
else:
    print('Não é possível criar um Triângulo.')
print('\033[0;31m=-=-=- FIM -=-=-=\033[m')
