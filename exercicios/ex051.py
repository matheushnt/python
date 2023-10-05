from time import sleep
print('\033[1;35m=-=-=-= PROGRESSÃO ARITMÉTICA =-=-=-=\033[m')
primeiro = int(input('Qual o primeiro o termo: '))
razao = int(input('Qual razão: '))
n = 10

ultimo = primeiro + (n-1) * razao
"""
ultimo = An (termo enésimo)
primeiro = A₁ (primeiro termo)
n = quantidade de termos, mas An é um termo genérico
-1 = número da posição do termo An -1
razao = constante
"""
ultimo = ultimo + 1
# o Python sempre ignora o último termo do loop FOR, somando com 1 ele não ignora

for pa in range(primeiro, ultimo, razao):
    print(pa)
    sleep(0.08)
print('\033[1;35m=-=-=-= PROGRESSÃO ARITMÉTICA =-=-=-=\033[m')
