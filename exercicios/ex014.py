c = float(input('Informe a temperatura em °C: '))
f = (c * 1.8) + 32
print(f'A temperatura de {c:.1f}°C corresponde a {f:.1f}°F!')

farenheit = float(input('Informe a temperatura en °F: '))
celsius = (farenheit - 32) / 1.8
print(f'A temperatura de {farenheit:.1f}°F corresponde a {celsius:.1f}°C!')
