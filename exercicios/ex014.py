c = float(input('Informe a temperatura em °C: '))   # lê a entrada de dados
f = (c * 1.8) + 32      # converte celsius para farenheit
print(f'A temperatura de {c:.1f}°C corresponde a {f:.1f}°F!')       # exibe a resposta

farenheit = float(input('Informe a temperatura en °F: '))   # lê a entrada de dados
celsius = (farenheit - 32) / 1.8        # converte farenheit para celsius
print(f'A temperatura de {farenheit:.1f}°F corresponde a {celsius:.1f}°C!')     # exibe a resposta
