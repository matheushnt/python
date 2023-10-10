print('\033[1;30;107m------ Detector de Palíndromo ------\033[m')
frase = str(input('Digite uma frase:\n'))
fraseTratada = frase.lower().replace(' ', '')       # transforma tudo para minúsculo e retira os espaços
fraseInvertida = fraseTratada[::-1]         # inverte a ordem da string usando a indexação negativa
print(f'{fraseTratada} é {fraseInvertida}')
if fraseTratada == fraseInvertida:
    print('É um Palíndromo')
else:
    print('Não é um Palíndromo.')
print('\033[1;30;107m------ FIM ------\033[m')
