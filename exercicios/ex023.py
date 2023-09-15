num = int(input('Digite um número: '))
un = num // 1 % 10              # resulta na unidade do valor digitado
dez = num // 10 % 10            # resulta na dezena do valor digitado
cent = num // 100 % 10          # resulta na centena do valor digitado     
milhar = num // 1000 % 10       # resulta no milhar do valor digitado
print(f'Unidade: {un}')
print(f'Dezena: {dez}')
print(f'Centena: {cent}')
print(f'Milhar: {milhar}')
