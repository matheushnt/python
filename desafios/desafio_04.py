dado = input('Digite qualquer coisa: ')     # lê os dados de entrada
print('O dado digitado é do tipo: {}'.format(type(dado)))   # exibe o tipo primitivo do dado inserido
print('O dado digitado é númerico? Resposta: {}'.format(dado.isnumeric()))      # verifica e exibe se o dado é numérico
print('O dado digitado é alfabético? Resposta: {}'.format(dado.isalpha()))      # verifica e exibe se o dado é alfabético
print('O dado digitado é alfanumérico? Resposta: {}'.format(dado.isalnum()))    # verifica e exibe se o dado é alfanumérico