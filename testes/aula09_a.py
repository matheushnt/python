frase01 = 'Curso em Vídeo Python'
print(frase01[3])       # retorna o caractere do índice 3

print(frase01[0:14])        # retorna os caracteres entre o índice 0 a 13 (o caractere do índice 14 não irá aparecer)

print(frase01[9:20:3])      # retorna os caracteres entre o índice 9 a 19 pulando de três em três caracteres

print(frase01[:20])         # início não explicitado, portanto irá retornar os caracteres entre 0 a 19 (o caractere do índice 20 não irá aparecer)

print(frase01[0:])          # fim não explicitado, portanto irá retornar os caracteres entre 0 a 20

print(frase01[::2])         # início e fim não explicitados, portanto irá retornar toda a string pulando de dois em dois

print("""Lorem ipsum dolor sit amet, consectetur adipiscing elit.       
Morbi consequat diam quis felis condimentum rhoncus. 
Maecenas libero est, hendrerit non vestibulum a, pharetra ut purus. 
Donec rutrum sapien vel nulla eleifend scelerisque.""")         # retorna a string da exata forma que foi formatada

print(frase01.count('o'))       # conta a quantidade do caractere "o" na string

print(frase01.upper().count('O'))       # transforma a string toda para MAIÚSCULAS e conta a quantidade de caracteres "O" em MAIÚSCULO

print(len(frase01))     # retorna o tamanho da string

frase02 = '   Curso em Vídeo JavaScript   '

print(len(frase02))     # retorna o tamanho da string

print(len(frase02.strip()))         # elimina todos os espaços inúteis

print(frase02.rstrip())             # elimina todos os espaços inúteis a direita

print(frase02.lstrip())             # elimina todos os espaços inúteis a esquerda

print(frase02.replace('JavaScript', 'Java'))        # substitue JavaScript por Java

frase02 = frase02.replace('JavaScript', 'Java')     # substitue JavaScript por Java, mas é atribuido a variável, assim mudando a string

print(frase02)      # exibe a string

"""
Uma string, em seus microelementos são imutáveis, a não ser que seja utilizado uma função de transformação de string e faça uma atribuição
"""

print('Curso' in frase02)       # procura o caractere desejado na string e retorna True
print('vídeo' in frase02)       # procura o caractere desejado na string e retorna False

print(frase01.find('Curso'))            # encontra o caractere desejado na string e retorna índice onde começa
print(frase01.find('vídeo'))            # procura o caractere desejado na strig e retorna -1 pois não encontrou   
print(frase01.lower().find('vídeo'))

print(frase02.split())           # divide a string fazendo uma quebra onde há espaços, tornando-se uma lista de strings
dividido = frase02.split()       # recebe a string dividida em formato de lista    
print(dividido[0])               # retorna a string dentro da lista com seu respectivo índice
print(dividido[3])               # retorna a string dentro da lista com seu respectivo índice
print(dividido[3][0])            # retorna o caractere dentro da string que está na lista

print('-'.join(frase01))         # retorna a string com a junção de "-" entre cada caractere
