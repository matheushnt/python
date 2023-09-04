real = float(input('Quanto de dinheiro você tem na carteira? \nR$ '))   # lê a entrada de dados
dolar = real / 4.94     # efetua o cálculo da cotação do dólar
print(f'Com R$ {real:.2f} você poderá comprar US$ {dolar:.2f}')     # exibe o resultado
