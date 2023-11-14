print('+-+' * 15)
print(f'{'LISTA ORDENADA SEM REPETIÇÕES':^45}')
print('+-+' * 15)
valores = list()    # lista vazia
for cont in range(0, 5):    # laço de 5 cinco requisições
    valor = int(input('Digite um número: '))    # entrada de dados 
    if cont == 0 or valor > valores[-1]:    # se o contador for igual ao primeiro número digitado ou se o número digitado for maior que os números já adicionados, esse novo número será adicionando na lista
        valores.append(valor)
    else:   # senão se esse número for menor que algum número digitado ou maior que outro número já digitado, será feito uma varredura na lista
        posicao = 0
        while posicao < len(valores):   # percorre a lista analisando-a
            if valor <= valores[posicao]:   # se VALOR DIGITADO <= N1, será adicionado no lugar desse número já existente na lista
                valores.insert(posicao, valor) 
                break  # interrompe a lista caso a condição for atendida
            posicao += 1
print('+-+' * 10)
print(f'Os valores digitados em ordem foram: {valores}')
print('+-+' * 10)
