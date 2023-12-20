def maior(* lst):   # Definindo uma função com desempacotamento
    pos = 0
    while pos < len(lst):   # Laço para percorrer a Tupla com os parâmetros
        if pos == 0 or lst[pos] > m:    # Verificação do maior número
            m = lst[pos]  
        pos += 1  
    print(f'Números informados: {lst}. Maior número informado: {m}')


""" PROGRAMA PRINCIPAL """
maior(50, 33, 42, 2, 3)
maior(69, 27, 28, 13, 21)
maior( 35, 12, 38, 10, 16)
