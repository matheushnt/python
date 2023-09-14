frase01 = 'Curso em Vídeo Python'
print(frase01[3])

print(frase01[0:14])

print(frase01[9:20:3])

print(frase01[:20])

print(frase01[0:])

print(frase01[::2])

print("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Morbi consequat diam quis felis condimentum rhoncus. 
Maecenas libero est, hendrerit non vestibulum a, pharetra ut purus. 
Donec rutrum sapien vel nulla eleifend scelerisque.""")

print(frase01.count('o'))

print(frase01.upper().count('O'))

print(len(frase01))

frase02 = '   Curso em Vídeo JavaScript   '

print(len(frase02))

print(len(frase02.strip()))

print(frase02.rstrip())

print(frase02.lstrip())

print(frase02.replace('JavaScript', 'Java'))

frase02 = frase02.replace('JavaScript', 'Java')

print(frase02)

"""
Uma string, em seus microelementos são imutáveis, a não ser que seja utilizado uma função de transformação de string e faça uma atribuição
"""

print('Curso' in frase02)
print('vídeo' in frase02)

print(frase01.find('Curso'))
print(frase01.find('vídeo'))
print(frase01.lower().find('vídeo'))

print(frase02.split())
dividido = frase02.split()
print(dividido[0])
print(dividido[3])
print(dividido[3][0])

print('-'.join(frase01))
