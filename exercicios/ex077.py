palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for palavra in palavras:    # o laço itera dentro da tupla PALAVRAS retornando a informação desejada na var PALAVRA
    print(f'\nNa palavra {palavra.upper()} temos: ', end='')
    for letra in palavra:   # cada palavra é uma lista, por isso o laço itera dentro da var PALAVRA
        if letra.lower() in 'aeiou':    # depois da iteração, a var LETRA recebe a letra de cada palavra
            print(letra, end=' ')
