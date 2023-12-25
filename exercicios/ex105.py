def turma(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param n: notas informadas
    :param sit: (Opcional) mostra ou não a situação da turma
    :return: retorna o Dicionário com informações da turma
    """
    # Total de alunos informados
    alunos = {'Total de Alunos': len(n)}
    # Variáveis utilizadas na Estrutura While
    maior = 0
    menor = 0
    soma = 0
    c = 0
    # Laço para verificar a maior e menor nota e também soma cada nota
    while c < len(n):
        if c == 0 or n[c] > maior:
            maior = n[c]
        if c == 0 or n[c] < menor:
            menor = n[c]
        soma += n[c]
        c += 1
    alunos['Maior Nota'] = maior
    alunos['Menor Nota'] = menor
    # Cálculo da média da turma
    alunos['Média'] = soma / alunos['Total de Alunos']
    # Se houver necessidade de exibir a situação da turma, será exibida
    if sit:
        if alunos['Média'] <= 4:
            alunos['Situação'] = 'RUIM'
        elif alunos['Média'] <= 7:
            alunos['Situação'] = 'BOM'
        else:
            alunos['Situação'] = 'ÓTIMO'
    return alunos


# Programa principal
print('=-'*15)
print(f'{'SITUAÇÃO DE UMA TURMA'}')
print('=-'*15)
resp = turma(10, 1, 6, 3, 8, 7, 10, 9, sit=True)
# Exibe cada chave-valor do Dicionário
for k, v in resp.items():
    print(f'{k}: {v}')
    print('-'*15)
