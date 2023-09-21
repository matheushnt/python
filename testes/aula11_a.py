print('\033[1;33mOlá, Mundo!\033[m')

a = 10
b = 20
soma = a + b
print(f'A soma entre os valores \033[1;33m{a}\033[m e \033[1;34m{b}\033[m é igual a \033[1;31m{soma}\033[m')

nome = 'Matheus'
print(f'Prazer em te conhecer \033[4;36m{nome}\033[m')

cores = {
    'limpa': '\033[m',
    'preto': '\033[0;30m',
    'branco': '\033[0;97m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m',
    'roxo': '\033[0;35m',
    'ciano': '\033[0;36m',
    'cinza': '\033[0;37m'}

pessoa = str(input('Qual o seu nome?\n'))
print(f'Bem vindo, {cores["verde"]}{pessoa}{cores["limpa"]}')

"""
Códigos para estilização (ANSI)
\033[;;m
\033[m

Style:
>> 0 - none
>> 1 - bold
>> 4 - underline
>> 7 - negative

Text:
>> 30 - preto
>> 31 - vermelho
>> 32 - verde
>> 33 - amarelo
>> 34 - azul
>> 35 - roxo
>> 36 - ciano
>> 37 - cinza
>> 97 - branco

Background:
>> 40 - preto
>> 41 - vermelho
>> 42 - verde
>> 43 - amarelo
>> 44 - azul
>> 45 - roxo
>> 46 - ciano
>> 47 - cinza
>> 107 - branco
"""
