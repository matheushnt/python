# Tente fazer isso...
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    div = a / b
# Caso aconteça um Erro de Valor ou Erro de Tipo, dispara uma Exceção
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')

# Caso a divisão tente ser realizada por zero, dispara uma Exceção
except ZeroDivisionError:
    print('Não é possível fazer uma divisão por zero.')

# Caso o usuário não queira inserir dados, dispara uma Exceção
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
