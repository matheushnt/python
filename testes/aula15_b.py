# loop infinito, porém com flag
n = s = 0
while n != 999:
    s += n
    n = int(input('Digite um número: '))
print('A soma vale {}'.format(s))
