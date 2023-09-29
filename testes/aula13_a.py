from time import sleep
print('Oi!')
print('Oi!')
print('Oi!')
print('Oi!')
print('Oi!')
print('Oi!')
sleep(1)
for c in range(1,6):        # repetirá 5 vezes, quando chegar no 6, encerra-se a repetição
    print('Oi!')
    print('Bom dia!')
print('FIM')

for contador in range(1, 11):       # cada numero da repeticao, vai ser atribuido a variavel de controle "contador"
    print(contador)
    sleep(0.3)
print('Fim do laço')    

for regressivo in range(10, 0, -1):     # o ultimo numero do meu range, diz respeito ao incremento, ou seja, a cada iteracao, vai ser removido ou adicionado um numero especificado no incremento
    print(regressivo)
    sleep(0.3)
print('Fim do laço')    

for progressivo in range(0, 12, 2):     # a iteração sera feita de 2 em 2
    print(progressivo)
    sleep(0.3)
print('Fim do laço')
