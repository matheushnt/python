soma = produtos = produtos_caros = cont = menor = 0
barato = ''
print('=' * 60)
print(f'{'LOJA SUPER BARATÃO':^60}')
print('=' * 60)
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    print('-' * 60)
    cont += 1   # quantifica os produtos
    soma += preco   # calcula o total dos valores dos produtos
    if preco > 1000:    # verifica se o preço é acima de 1000
        produtos_caros += 1
    if cont == 1 or preco < menor:  # o primeiro produto é ovalor mais barato. Se o novo preço informado for menor que o primeiro preço (barato), menor recebe o novo menor preço
        menor = preco
        barato = produto    # recebe o nome do produto do produto mais barato
    resposta = str(input('Quer continuar [S/N] ?\n')).strip()[0]
    while resposta not in 'SsNn':
        resposta = str(input('Quer continuar [S/N] ?\n')).strip()[0]
    if resposta in 'Nn':
        break
    print('-' * 60)
print('=' * 60)
print(f'O total da compra foi R$ {soma:.2f}')
print(f'Temos {produtos_caros} custando acima de R$ 1000.00')
print(f'O produto mais barato é o(a) {barato} que custa R$ {menor:.2f}')
