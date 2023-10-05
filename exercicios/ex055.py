from time import sleep
ListaDePesos = []
for Peso in range(1, 5+1):
    Pesos = float(input('Informe seu peso: '))
    ListaDePesos.append(Pesos)      # adiciona um elemento no final de uma de uma lista
print('PROCESSANDO...')
sleep(0.5)
print(f'O menor peso é {min(ListaDePesos)}')       # o método min() encontra o menor valor dentro de uma ListaDePesos
print(f'O maior peso é {max(ListaDePesos)}')       # o método max() encontra o maior valor dentro de uma ListaDePesos
print(f'A soma de todos os pesos é igual a {sum(ListaDePesos)}')
