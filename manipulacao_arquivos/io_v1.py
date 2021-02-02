#!/usr/local/bin/python3
arquivo = open('pessoas.csv')
dados = arquivo.read()
# lê o arquivo e colocando todos os valores na variável dados ocupando memória
arquivo.close()
for registro in dados.splitlines():
    # separa os dados lidos do arquivos separando-os por linhas
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))
    # registro.split(',') separa os valores de cada linha
    # delimitados por virgulas
