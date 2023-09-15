num = int(input('Digite um número: '))
un = num // 1 % 10              
dez = num // 10 % 10            
cent = num // 100 % 10               
milhar = num // 1000 % 10       
print(f'Unidade: {un}')
print(f'Dezena: {dez}')
print(f'Centena: {cent}')
print(f'Milhar: {milhar}')
