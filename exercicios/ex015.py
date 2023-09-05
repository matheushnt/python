dias = int(input('Por quantos dias o carro foi alugado?\n'))
km = float(input('Quantos KM rodados?\n'))
precoCar = 60 * dias
precoKM = 0.15 * km
total = (60 * dias) + (0.15 * km)
print(f'O preço total a pagar pelo aluguel é: R$ {total:.2f}')