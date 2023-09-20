reta01 = float(input('Informe o comprimento da primeira reta: '))
reta02 = float(input('Informe o comprimento da segunda reta: '))
reta03 = float(input('Informe o comprimento da terceira reta: '))
if reta01 < (reta02 + reta03) and reta02 < (reta01 + reta03) and reta03 < (reta01 + reta02):        # Para criar um triângulo, há uma regra chamada Condição de Existência que diz: um lado tem que ser menor que a soma dos outros dois lados
    print('Com os comprimentos informados, é possível criar um Triângulo.')
else:
    print('Com os comprimentos informados, não é possível criar um Triângulo.')
