times = ('Botafogo', 'Palmeiras', 'Bragantino', 'Grêmio', 'Flamengo', 'Atlético-MG', 'Athletico-PR', 'Fluminense', 'Fortaleza', 'Cuiabá', 'São Paulo', 'Internacional', 'Cruzeiro', 'Corinthians', 'Bahia', 'Santos', 'Goiás', 'Vasco da Gama', 'Coritiba', 'América-MG')
print(f'Os 5 primeiros colocados são: {times[:5]}')
print(f'Os times do Z4 são: {times[16:]}')
times_organizados = sorted(times)
print(f'Os times organizados por ordem alfabética são: {times_organizados}')
print(f'O Fortaleza está na {times.index('Fortaleza') + 1}º posição')
