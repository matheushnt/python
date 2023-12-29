def ler_dinheiro(msg):
    while True:
        # Dispara a solicitação do preço, fazendo um Tratamento de Erros
        num = input(msg).replace(',', '.').strip()
        # Caso seja inserido uma informação diferente de número, dispara um erro
        if num.isalpha() or num == '':
            print(f'ERRO: "{num}" é um preço inválido.')
        else:
            # Com o comando return, interrompe o laço
            return float(num)
