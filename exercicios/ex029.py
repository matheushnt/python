velocidade = int(input('Informe a velocidade que você estava trafegando na pista:\n'))
if velocidade > 80:
    print(f'Aviso de Multa por Excesso de Velocidade. Você estava acima de 80Km/h.')
    multa = (velocidade - 80) * 7
    print(f'A multa será no valor de R$ {multa:.2f}')
else:
    print('Parabéns pela sua condução segura e por fazer a diferença nas estradas.')