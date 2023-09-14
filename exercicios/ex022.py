nome = str(input('Qual o seu nome?\n'))
print(f'Seu nome em maiúsculo: {nome.upper()}')     # transforma a string toda para maiúscula
print(f'Seu nome em minúsculo: {nome.lower()}')     # transforma a string toda para minúscula
print(f'Seu nome possui {len(nome.replace(" ", ""))} letras')       # .replace() está retirando todos os espaços em branco
dividido = nome.split()     # recebe o valor da variável nome fatiado, cada palavra possui um índice dentro da lista
print(f'Seu primeiro nome tem {len(dividido[0])} letras')      # exibe a quantidade de letras do primeiro nome da pessoa
# .split() divide a string por palavras e são inseridas dentro de uma lista. Cada palavra possui um índice
