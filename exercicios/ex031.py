print('--- Análise de Distância ---')
distancia = int(input('Qual a distância em KM entre o início e o seu destino: '))
if distancia <= 200:
    custo = distancia * 0.5     # calcula o custo em reais da passagem
    print(f'Sua viagem custará R$ {custo:.2f}')
else:
    custo = distancia * 0.45         # calcula o custo em reais da passagem
    print(f'Sua viagem custará R$ {custo:.2f}')
print('-------- FIM --------')
