def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos +=1
    print(lst)


lista = [2, 5, 9, 6, 3, 4]
dobra(lista)
