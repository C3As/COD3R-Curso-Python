PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')
# boas práticas em python recomendam que constantes sejam declaradas em maiusculas, apesar de não existir constantes no python

textos = [
    'João gosta de futebol e política',
    'A praia foi divertida'
]

for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possui pelo menos uma palavra proibida:', palavra)
            break
    else:
        print('Texto autorizado:', texto)
