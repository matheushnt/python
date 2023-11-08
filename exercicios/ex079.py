valores = list()
while True:
    valor = int(input('Digite um número: '))
    valores.append(valor)
    resp = str(input('Você quer continuar? [S/N]\n'))[0].strip().upper()
    if resp not in 'SN':    # validação dos dados
        while resp not in 'SN':     # enquanto a resposta for diferente de S ou N...
            resp = str(input('Você quer continuar? [S/N]\n'))[0].strip().upper()
    if resp in 'N':     # se a resposta for N, o laço é encerrado
        break
valores_unicos = list(set(valores))
print(f'Os valores digitados foram: {valores_unicos}')
