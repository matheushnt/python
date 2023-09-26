estilo = {
    'roxo': '\033[1;35m',
    'amarelo': '\033[1;33m',
    'azul': '\033[1;34m',
    'sublinhado': '\033[4m',
    'limpa': '\033[m'}      # dicionário com estilos

nome = str(input('Qual o seu nome?\n'))
if nome == 'Matheus':
    print(f'Que nome lindo {estilo["roxo"]}{nome}{estilo["limpa"]}')

elif nome == 'Henrique' or nome == 'Gislane':       # Estrutura Condicional Aninhada
    print(f'Te desejo um ótimo dia, {estilo["azul"]}{nome}{estilo["limpa"]}')

elif nome in 'Kelcianne da Silva Nunes' or 'Francisca Meiriele Amaro Ferreira':       # Estrutura Condicional Aninhada
    print(f'Que belo nome feminino você tem {estilo["sublinhado"]}{estilo["azul"]}{nome}{estilo["limpa"]}')
    
else:       # o else é opcional
    print(f'Tenha um Bom Dia, {nome}')
