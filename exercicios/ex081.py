numeros = []
while True:
    num = int(input('Digite um número [999 para PARAR]: '))
    if num == 999:
        break
    numeros.append(num)
print(f'Foram digitados {len(numeros)} números')
print(f'Os valores organizados de forma decrescente: {sorted(numeros, reverse=True)}')
if 5 in numeros:
    print(f'O números 5 está na posição {numeros.index(5)}')
else:
    print('O número 5 não foi digitado')
