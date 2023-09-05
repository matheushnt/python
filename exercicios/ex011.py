comprimento = float(input('Qual o comprimento da parede? \n'))      # lê a entrada de dados
altura = float(input('Qual a altura da parede? \n'))        # lê a entrada de dados
area = comprimento * altura     # calcula a área da parede
tinta = area / 2    # calcula a quantidade de tinta necessária para pintar a parede levando em consideração que, a cada d 2m², utiliza-se 1L de tinta
print(f'A área da parede é: {area:.2f}')    # exibe a resposta
print(f'Para pintar essa parede, você precisará de {tinta:.3f} litros')     # exibe a resposta