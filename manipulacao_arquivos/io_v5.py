#!/usr/local/bin/python3

# O bloco WITH garante que após abertura e leitura do arquivo
# o mesmo será fechado

with open('pessoas.csv') as arquivo:
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

if arquivo.close:
    print('Arquivo fechado')
