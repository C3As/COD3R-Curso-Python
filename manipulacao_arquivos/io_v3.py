#!/usr/local/bin/python3
arquivo = open('pessoas.csv')
for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
    # strip() - retira os espaços vazios
arquivo.close()
