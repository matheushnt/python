dias = int(input('Por quantos dias o carro foi alugado?\n'))    # lê a entrada de dados
km = float(input('Quantos KM rodados?\n'))     # lê a entrada de dados
total = (60 * dias) + (0.15 * km)   # calcula o preço do aluguel dp carro
print(f'O preço total a pagar pelo aluguel é: R$ {total:.2f}')      # exibe a resposta