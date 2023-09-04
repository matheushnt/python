metro = int(input('Digite um valor em METROS: '))  #lê a entrada de dados
kilometro = metro / 1000  # divide por 1000
hectometro = metro / 100  # divide por 100
decametro = metro / 10    # divide por 10
decimetro = metro * 10    # multiplica por 10
centimetro = metro * 100  # multiplica por 100
milimetro = metro * 1000  # multiplica por 1000
print(f'KM: {kilometro} \nHM: {hectometro} \nDAM: {decametro} \nM: {metro} \nDM: {decimetro} \nCM: {centimetro} \nMM: {milimetro}')  # exibe a resposta