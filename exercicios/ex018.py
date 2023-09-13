from math import cos, sin, tan, radians       # importando as funções de cosseno, seno, tangente e radianos
ang = float(input('Informe um ângulo qualquer: '))
print(f'O Seno é igual a {sin(radians(ang)):.2f}')      # primeiramente converte o ângulo para radianos para então realizar o cálculo do Seno
print(f'O Cosseno é igual a {cos(radians(ang)):.2f}')       # primeiramente converte o ângulo para radianos para então realizar o cálculo do Cosseno
print(f'A Tangente é igual a {tan(radians(ang)):.2f}')      # primeiramente converte o ângulo para radianos para então realizar o cálculo da Tangente
