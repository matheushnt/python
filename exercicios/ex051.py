primeiro = int(input('Qual o primeiro o termo: '))
razao = int(input('Qual razão: '))
n = 10

ultimo = primeiro + (n-1) * razao
ultimo = ultimo + 1

for pa in range(primeiro, ultimo, razao):
    print(pa)
