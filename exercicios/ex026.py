import unicodedata
frase = str(input('Digite uma frase qualquer:\n')).strip()
fraseSemAcento = unicodedata.normalize("NFD", frase)
fraseSemAcento = fraseSemAcento.encode("ascii", "ignore")
fraseSemAcento = fraseSemAcento.decode("utf-8")
print(f'A letra "A" aparece {fraseSemAcento.lower().count("a")} vezes')
print(f'A primeira vez que ela aparece é no índice {fraseSemAcento.find("a") + 1}')
print(f'A última vez que ela aparece é no índice {fraseSemAcento.rfind("a") + 1}')      # o método .rfind() começará a prucurar a primeira letra "A" a partir da direita, o inverso ocorre com .lfind()

# o uso do + 1 após o .find() é para a numeração se adequar para nossa leitura

# importando a biblioteca unicodedata nativa do Python, é possível tornar os caracteres padrões, sem acentos
