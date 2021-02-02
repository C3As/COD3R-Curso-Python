#!/usr/local/bin/python3

# Em caso de erros após o arquivo ter sido aberto há um risco do a
# rquivo permanecer aberto, neste caso usando try & finally mesmo
# que ocorra o erro o bloco de finally será executado

try:
    arquivo = open('pessoas.csv')
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
finally:
    arquivo.close()
