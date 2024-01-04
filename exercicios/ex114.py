# Importação dos módulos da Lib padrão do Python
from urllib import request, error

# Tentativa de acessar o site GitHub
try:
    site = request.urlopen('https://github.com')

# Caso o site não esteja acessível, dispara uma Exceção
except error.URLError:
    print('O site GitHub não está acessível no momento.')

# Caso o site esteja acessível, o programa encerra com êxito
else:
    print('O site GitHub está acessível.')
