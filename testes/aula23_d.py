# Tente fazer isso...
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    div = a / b
# Se ocorrer uma falha, execute isso...
except Exception as erro:   # Criando a variável "erro" para exibir a classe da Exception
    # Exibindo a classe da Exceção
    print(f'O problema encontrado foi {erro.__class__}')
# Se der tudo certo, execute isso...
else:
    print(f'O resultado é igual a {div:.2f}')
# Independente se der certo ou falhar, execute isso...
finally:
    print('Volte sempre. Até logo!')
