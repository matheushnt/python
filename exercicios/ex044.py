from time import sleep
print('\033[1;32m=-=-=- GERENCIADOR DE PAGAMENTOS -=-=-=\033[m')
preco = float(input('Qual o preço do produto: R$ '))
condicao = int(input('Digite 1 para pagamento à vista com dinheiro ou cheque. \nDigite 2 para pagamento à vista no cartão. \nDigite 3 para pagamento parcelado em até 2x no cartão. \nDigite 4 para pagamento parcelado em 3x ou mais no cartão.\n'))
print('CALCULANDO PREÇO...')
sleep(2)
if condicao == 1:
    desconto = preco - (preco * 10 / 100)       
    precoNovo = desconto
    print(f'À vista usando dinheiro ou cheque, você receberá um desconto de 10% e  pagará {precoNovo}')
elif condicao == 2:
    desconto = preco - (preco * 5 / 100)
    precoNovo = desconto
    print(f'À vista usando cartão, você receberá um desconto de 5% de desconto e pagará {precoNovo}')
elif condicao == 3:
    parcela = preco / 2
    print(f'Parcelando em até 2x você pagará o preço normal sem desconto. As parcelas serão de {parcela:.2f} cada.')
elif condicao == 4:
    acrescimo = preco + (preco * 20 / 100)
    precoNovo = acrescimo
    print(f'Parcelando em 3x ou mais, pagará com juros. O novo preco será {precoNovo}')
print('\033[1;34m=-=-=- FIM -=-=-=\033[m')
