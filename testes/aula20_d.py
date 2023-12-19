def contador(* num):    # o símbolo asterísco (*) serve para desempacotar os valores do parâmetro
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')


""" PROGRAMA PRINCIPAL """
contador(2, 4, 6, 8, 10)    # Empacotando os valores do parâmetro
contador(9, 3, 1, 5)    # Empacotando os valores do parâmetro
contador(3, 1, 10, 5, 9, 2)    # Empacotando os valores do parâmetro
