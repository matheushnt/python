impar = par = 0     # as variáveis impar e par recebem zero
numero = 1  # inicialização
while numero != 0:      # condição de parada
    if numero != 0:
        numero = int(input('Digite um número: '))
        if numero % 2 == 0:
            par += 1    # incrementa 1 na variável par
        else:
            impar += 1  # incrementa 1 na variável impar
print(f'Foram informados {impar} números ímpares e {par} números pares.')
