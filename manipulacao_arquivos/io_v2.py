#!/usr/local/bin/python3
arquivo = open('pessoas.csv')
# dados lidos não foram armazenados em nenhuma variável - não ocupa memória
for registro in arquivo:
    # separa os dados lidos do arquivos separando-os por linhas
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))
    # registro.split(',') separa os valores de cada linha
    # delimitados por virgulas
arquivo.close()
