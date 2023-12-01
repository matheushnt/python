from datetime import date
print('= ='*15)
print(f'{'CADASTRO DE TRABALHADOR EM PYTHON':^45}')
print('= ='*15)
ano_atual = date.today().year   # obter o ano atual do sistema
cadastro = {}
cadastro['Nome'] = str(input('Nome: '))
idade = int(input('Ano de Nascimento: '))
idade = ano_atual - idade   # cálculo da idade do trabalhador
cadastro['Idade'] = idade
cadastro['CTPS'] = str(input('Carteira de Trabalho (0 não tem): '))
if cadastro['CTPS'] == '0':
    print('= ='*10)
    for chave, valor in cadastro.items():
        print(f'{chave} = {valor}')
else:
    cadastro['Contratação'] = int(input('Ano de contratação: '))
    cadastro['Salário'] = float(input('Salário: R$ '))
    aposentadoria = ano_atual - cadastro['Contratação'] # calcula o tempo de contribuição
    aposentadoria = 35 - aposentadoria  # calcula quanto tempo falta para se aposentar
    cadastro['Aposentadoria'] = aposentadoria + cadastro['Idade']   # exibe com quantos anos o trabalhador vai se aposentar
    print('= ='*10)
    for chave, valor in cadastro.items():
        print(f'{chave} = {valor}')
    if cadastro['Idade'] >= cadastro['Aposentadoria']:  # exibe uma mensagem caso o trabalhador já possa se aposentar
        print(f'Você já pode se aposentar, {cadastro["Nome"]}')
