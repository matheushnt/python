print('=-' * 20)
print(f'{'ANÁLISE DE DADOS COM TUPLA':^40}')
print('=-' * 20)
valores = (int(input('Primeiro valor: ')),
           int(input('Segundo valor: ')),
           int(input('Terceiro valor: ')),
           int(input('Quarto valor: ')))
if 5 in valores:
    print(f'O número 5 apareceu {valores.count(5)} vez(es)')
else:
    print(f'O número 5 apareceu nenhuma vez')
print('=' * 40)
if 3 in valores:
    print(f'O número 3 está na {valores.index(3) + 1}° posição')
else:
    print('O número 3 apareceu nenhuma vez')
print('=' * 40)
pares = 0
for contador in range(0, len(valores)):
    if valores[contador] % 2 == 0:
        print(f'O número {valores[contador]} é par')
        pares += 1
print('=' * 40)
if pares == 0:
    print(f'Não apareceu nenhuma vez valores pares')
