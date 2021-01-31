PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'política'}
# boas práticas em python recomendam que constantes sejam declaradas em maiusculas, apesar de não existir constantes no python

textos = [
    'João gosta de futebol e política',
    'A praia foi divertida'
]

# ao trocal PALAVRAS_PROIBIDAS de tupla para set(conjunto) podemos usar as funcionalidades de set
# e uma delas é a intersecao ou seja o dentro de textos está também dentro de PALAVRAS_PROIBIDAS

for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print('Texto possui pelo menos uma palavra proibida:', intersecao)
    else:
        print('Texto autorizado:', texto)
