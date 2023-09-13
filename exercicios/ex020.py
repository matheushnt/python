from random import shuffle
al1 = str(input('Qual o nome do primeiro aluno: '))
al2 = str(input('Qual o nome do segundo aluno: '))
al3 = str(input('Qual o nome do terceiro aluno: '))
al4 = str(input('Qual o nome do quarto aluno: '))
alunos = [al1, al2, al3, al4]
shuffle(alunos)
print('A ordem de apresentação será: ')
print(alunos)
