nome = str(input('Digite seu nome completo: \n')).strip()
nomeFatiadoEu = nome.split()
nomeMãe = str(input('Digite o nome completo da sua Mãe: \n')).strip()
nomeFatiadoMãe = nomeMãe.split()
print(f'Seu primeiro nome é: {nomeFatiadoEu[0]}')
print(f'Seu último nome é: {nomeFatiadoEu[len(nomeFatiadoEu) - 1]}')      # "nomeFatiadoEu[-1]" em Python, a indexação negativa começa do fim
print(f'O último nome da sua mãe é: {next(reversed(nomeFatiadoMãe))}')      # o método reversed() inverte a ordem da lista como um iterador. Já o método next() imprime o próximo elemento, neste caso o último elemento
