print('\033[1;33m=-=-=- VALIDAÇÃO DE DADOS -=-=-=\033[m')
sexo = str(input('Ingorme o seu sexo [M/F]: ')).upper()
if sexo != 'M' and sexo != 'F':     # se o sexo informado for diferente do solicitado, executa o laço 
    while sexo != 'M' and sexo != 'F':      # enquanto o dado informado for diferente do solicitado, executa o laço
        sexo = str(input('Dados inválidos. Por favor, informe novamente seu sexo: ')).upper()
        if sexo == 'M' or sexo == 'F':      # se o sexo informado for igual ao solicitado, termina o laço
            print(f'Sexo {sexo} cadastrado com sucesso.')
else:   # se sexo informado for igual ao solicitado, cadastrado é realizado com sucesso
    print(f'Sexo {sexo} cadastrado com sucesso.')
print('\033[1;31m=-=-=- FIM -=-=-=\033[m')
