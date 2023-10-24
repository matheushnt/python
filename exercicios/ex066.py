num = soma = 0
while True:     # o laço se torna infinito com o comando True
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break   # interrompe o laço caso a condição a seja verdadeira
    soma += num
print(f'A soma vale {soma}')
