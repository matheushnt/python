maiores = homens = mulheres = 0
while True:
    print('=' * 60)
    print(f'{'CADASTRE UMA PESSOA':^60}')
    print('=' * 60)
    idade = int(input('Idade: '))
    if idade > 18:
        maiores += 1    # quantidade de pessoas acima de 18 anos
    sexo = str(input('Sexo [M/F]: '))[0]
    while sexo not in 'FfMm':    # enquanto a resposta for diferente da esperada, itera o laço
        sexo = str(input('Sexo [M/F]: '))[0]
    if sexo in 'Mm':
        homens += 1     # quantidade de homens 
    if sexo in 'Ff' and idade < 20:
        mulheres += 1   # quantidade de mulheres menores de 20 anos
    print('-' * 60)
    resposta = str(input('Quer continuar?\n')).strip()[0]
    while resposta not in 'SsNn':   # enquanto a resposta for diferente da esperada, itera o laço
        resposta = str(input('Quer continuar?\n')).strip()[0]
    if resposta in 'Nn':
        break
print('~' * 60)
print(f'{'ESTATÍSTICAS':^60}')
print('~' * 60)
print(f'Total de pessoas com mais de 18 anos: {maiores}')
print(f'Ao todo são {homens} homens cadastrados')
print(f'E são {mulheres} mulheres com menos de 20 anos')
