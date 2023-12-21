def par(n):
    if n % 2 == 0:  # Se a condição for atendida, retorna VERDADEIRO
        return True
    else:   # Se a condição não for atendida, retorna FALSO
        return False


num = int(input('Digite um número: '))
if par(num):    # Se o retorno for VERDADEIRO, o número é par
    print(f'{num} é par!')
else:   # Se o retorno for FALSO, o número é ímpar
    print(f'{num} não é par!')
