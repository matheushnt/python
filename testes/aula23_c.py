# Tente fazer isso...
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    div = a / b
# Se ocorrer uma falha, execute isso...
except:
    print('Infelizmente ocorreu um erro ... 😭')
# Se der tudo certo, execute isso...
else:
    print(f'O resultado é igual a {div:.2f}')
# Independente se der certo ou falhar, execute isso...
finally:
    print('Volte sempre. Até logo!')
