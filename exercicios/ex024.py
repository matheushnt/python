nome = str(input('Digite o nome de uma cidade: ')).strip()
print(f'A cidade começa com o nome SANTO. Resposta: {nome[:5].upper() == "SANTO"}')     # exibe True se SANTO for o primeiro nome da cidade digitada, caso contrário, retorna False
