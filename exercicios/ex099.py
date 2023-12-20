from time import sleep


def maior(*num):  # Definindo uma função com desempacotamento
    print("= =" * 15)
    tam = len(num)
    if tam != 0:  # executa a análise se algum valor foi passado como parâmetro
        pos = 0
        while pos < tam:  # Laço para percorrer a Tupla com os parâmetros
            if pos == 0 or num[pos] > m:  # Verificação do maior número
                m = num[pos]
            pos += 1
        for valor in num:
            print(valor, end=" ", flush=True)
            sleep(0.3)
        print(f"=> Foram informados {tam} valores ao todo.")
        print(f"O maior valor informado foi o {m}")
    else:  # Não realiza a análise se nenhum valor foi passado como parâmetro
        print("Impossível análise. Nenhum valor informado.")


""" PROGRAMA PRINCIPAL """
maior(50, 33, 42, 2, 3)
maior(69, 27, 28, 21)
maior(38, 10, 16)
maior(90, 47)
maior()
