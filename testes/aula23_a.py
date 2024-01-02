# Tente fazer isso...
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    div = a / b
# Em caso de falha, execute isso...
except:
    print('Infelizmente tivemos um problema 😔')

print(f'O resultado é igual a {div}')
