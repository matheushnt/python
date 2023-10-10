resposta = 'S'  # inicialização
while resposta == 'S':  # condição de parada
    numero = int(input('Digite um número: '))
    resposta = str(input('Quer continuar? [S/N] ')).upper()
print('FIM')

""" Com o laço WHILE é possível criar situações onde eu faça laços indeterminadamente. Eu não preciso determinar um range() """
