#!/usr/local/bin/python3


with open('pessoas.csv',) as arquivo:
    with open('pessoas.txt', 'w') as saida:
        # open('pessoas.txt', 'w') o 'w' significa modo: escrita
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {}, Idade: {}'.format(*pessoa), file=saida)
            # file=saida o print será para um arquivo,
            # padrao do print é para a tela
if arquivo.close:
    print('Arquivo de entrada foi fechado')

if saida.close:
    print('Arquivo de saída foi fechado')
