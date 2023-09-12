from random import sample
al1 = str(input('Qual o nome do primeiro aluno: '))
al2 = str(input('Qual o nome do segundo aluno: '))
al3 = str(input('Qual o nome do terceiro aluno: '))
al4 = str(input('Qual o nome do quarto aluno: '))
alunos = [al1, al2, al3, al4]
print(f'O seguintes alunos irão se apresentar nessa ordem: \n{al1} será o {sample(4)}° \n{al2} será o {sample(4)}° \n{al3} será o {sample(4)}° \n{al4} será o {sample(4)}°')
