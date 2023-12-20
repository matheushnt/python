def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2   # Cada valor percorrido na lista será dobrado
        pos +=1
    print(lst)


""" PROGRAMA PRINCIPAL """
lista = [2, 5, 9, 6, 3, 4]  # Lista que servirá como um parâmetro
dobra(lista)    # lista passada como um parâmetro
