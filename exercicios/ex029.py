from time import sleep
print('=== Radar Eletrônico ===')
velocidade = float(input('Informe a velocidade que você estava trafegando na pista:\n'))
print('PROCESSANDO...')
sleep(3)        # O método sleep suspende a execução pelo número de segundos informado em seu parâmetro
if velocidade > 80:
    print(f'Aviso de Multa por Excesso de Velocidade. Você estava acima de 80Km/h.')
    multa = (velocidade - 80) * 7       # calcula a multa
    print(f'A multa será no valor de R$ {multa:.2f}')
else:
    print('Parabéns pela sua condução segura e por fazer a diferença nas estradas.')
print('===== FIM =====')
