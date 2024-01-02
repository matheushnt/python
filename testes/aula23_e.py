# Tente fazer isso...
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    div = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível fazer uma divisão por zero.')
except KeyboardInterrupt:
    print('Dados não informados')
# Se ocorrer uma falha genérica, execute isso...
except Exception as erro:
    # Exibindo a classe da Exceção
    print(f'O problema encontrado foi {erro.__cause__}')
# Se der tudo certo, execute isso...
else:
    print(f'O resultado é igual a {div:.2f}')
# Independente se der certo ou falhar, execute isso...
finally:
    print('Volte sempre. Até logo!')
