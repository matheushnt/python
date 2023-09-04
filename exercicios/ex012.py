preco = float(input('Qual o preço do produto? \n'))     # lê a entrada de dados
desconto = preco - (preco * 0.05)   # calcula a 5% em cima de do preço e subtrai esse resultado pelo preço do produto
print(f'Com desconto de 5%, preço ficará por {desconto:.2f}')   # exibe a resposta