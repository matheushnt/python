comprimento = float(input('Qual o comprimento da parede? \n'))
altura = float(input('Qual a altura da parede? \n'))
tinta = 4
area = comprimento * altura
print(f'A área da parede é: {area}')
print(f'Com 1L de tinta, é possível pintar {area % tinta} m quadrados')