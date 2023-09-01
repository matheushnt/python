dado = input('Digite qualquer coisa: ')     # lê os dados de entrada
print('O dado digitado é do tipo: {}'.format(type(dado)))   # exibe o tipo primitivo do dado inserido

print('O dado digitado é númerico? Resposta: {}'.format(dado.isnumeric()))      # verifica e exibe se o dado é numérico

print('O dado digitado é alfabético? Resposta: {}'.format(dado.isalpha()))      # verifica e exibe se o dado é alfabético

print('O dado digitado é alfanumérico? Resposta: {}'.format(dado.isalnum()))    # verifica e exibe se o dado é alfanumérico

print('O dado digitado são espaços? Resposta: {}'.format(dado.isspace()))    # verifica e exibe se o dado são somente espaços

print('O dado digitado está em Maiúsculas? Respota: {}'.format(dado.isupper()))     # verifica e exibe se o dado está em MAIÚSCULAS

print('O dado digitado está em minúsculas? Resposta: {}'.format(dado.islower()))    #  verifica e exibe se o dado está em minúsculas

print('O dado está capitalizado? Resposta: {}'.format(dado.istitle()))    # verifica e exibe se o dado está Capitalizado

# a variável dado é um objeto. Todo Objeto possui parâmentros e métodos