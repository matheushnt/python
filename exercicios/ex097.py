# Definindo as funções
def titulo(txt):    # Função de título
    print('='*30)
    print(f'{txt:^30}')
    print('='*30)


def escreva(msg):   # Função de mensagem personalizada
    tam_linha = len(msg) + 4    # configurando o tamanho da linha
    print(f'-'*tam_linha)
    print(f'  {msg}')
    print(f'-'*tam_linha)


""" PROGRAMA PRINCIPAL """
# Passando os parâmetros nas chamadas das funções
titulo('UM PRINT ESPECIAL')
escreva('Curso em Vídeo')
escreva('Aprendendo Python')
escreva('Matheus')
escreva('2023')
