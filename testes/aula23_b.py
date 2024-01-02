# Tente isso...
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    div = a / b
# Se der errado, faça isso...
except:
    print('Ocorreu um erro infelizmente... 😭')
# Se der certo, faça isso...
else:
    print(f'O resultado é igual a {div:.2f}')
