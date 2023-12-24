def lnum(msg):  # parâmetro formal
    cond = False
    valor = 0
    while True:
        global num
        num = str((input(msg)))
        if num.isnumeric():
            valor = int(num)
            cond = True
        else:
            print("\033[0;031mERRO! Digite um número inteiro válido.\033[m")
        if cond:
            break
    return valor


num = lnum('Digite um número: ')    # Chamada da função passando o parâmetro real
print(f'Você acabou de digitar o número {num}')
