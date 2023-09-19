from random import randint 
numAleatorio = randint(0, 5)
chute = int(input('Pensei em um número, tente acertá-lo.\n'))
print(f'O número que eu pensei foi: {numAleatorio}')
if chute == numAleatorio:
    print(f'PARABÉNS. Você acertou.')
else:
    print(f'Infelizmente você errou.')
