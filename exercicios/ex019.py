from random import choice       # importando apenas a função choice()
al1 = str(input('Informe o nome do primeiro estudante: '))
al2 = str(input('Informe o nome do segundo estudante: '))
al3 = str(input('Informe o nome do terceiro estudante: '))
al4 = str(input('Informe o nome do quarto estudante: '))
alunos = [al1, al2, al3, al4]       # esse array irá armazenar todos os nomes informados
print(f'O aluno(a) escolhido a apagar o quadro será: {choice(alunos)}')     # exibe um elemento aleatório a partir de uma sequência pelo método choice()
