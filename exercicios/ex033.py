print('***** Análise de Dados ******')
n1 = float(input('Digite um primeiro número: '))
n2 = float(input('Digite um segundo número: '))
n3 = float(input('Digite um terceiro número: '))
# Estrutura Condicional que verifica qual é o maior número
if n1 > n2 and n1 > n3:
    print(f'{n1} é o maior número.')
else:
    if n2 > n1 and n2 > n3:
        print(f'{n2} é o maior número.')
    else:
        if n3 > n1 and n3 > n2:
            print(f'{n3} é o maior número.')

# Estrutura Condicional que verifica qual é o menor
if n1 < n2 and n1 < n3:
    print(f'{n1} é o menor número.')
elif n2 < n1 and n2 < n3:
        print(f'{n2} é o menor número.')
elif n3 < n1 and n3 < n2:
            print(f'{n3} é o menor número.')
print('****** FIM ******')    
"""
Nas Estruturas Condicionais Aninhadas, existe o comando elif. Este comando é a junção do comando ELSE + IF que é utilizado nas Estruturas Condicionais Aninhadas
"""       
