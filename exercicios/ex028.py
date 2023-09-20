from random import randint      # nesse exercício, o método randint() atende melhor os requisitos
from time import sleep      # importando somente método sleep()
numAleatorio = randint(0, 5)        # retorna um valor inteiro entre 0 e 5
chute = int(input('Pensei em um número, tente acertá-lo.\n'))
print('PROCESSANDO...')
sleep(3)        # O método sleep suspende a execução do programa pelo número de segundos informado em seu parâmetro
print(f'O número que eu pensei foi: {numAleatorio}')
if chute == numAleatorio:
    print(f'PARABÉNS. Você acertou.')
else:
    print(f'Infelizmente você errou.')
# exibe a resposta de acordo com o resultado da comparação
print('===== FIM =====')
