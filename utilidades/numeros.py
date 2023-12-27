def fat(n):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f


def soma(*n):
    s = 0
    for v in n:
        s += v
    return s


def maior(lst):
    c = 0
    m = 0
    while c < len(lst):
        if c == 0 or lst[c] > m:
            m = lst[c]
        c += 1
    return print(m)


def menor(lst):
    c = 0
    m = 0
    while c < len(lst):
        if c == 0 or lst[c] < m:
            m = lst[c]
        c += 1
    return print(m)
