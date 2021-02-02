#!/usr/local/bin/python3

# Extrair o nono e o quarto campos do arquivo CSV sobre Região de
# influência das  Cidades do IBGE, que pode ser baixado em:
# http://www.geoservicos.ibge.gov.br/geoserver/wms?service=WFS&
# version=1.0.0&request=GetFeature&typeName=CGEO:RedeUrbanaSintese_Regic2007&
# outputFormat=CSV. ignorando a primeira linha que é o cabeçalho:
# O arquivo se encontra em ISO-8859-1 (aka latin1), será necessário
# usar o parâmetro encoding da função open

import csv
from urllib import request
# urllib é uma lib para trabalhar com url
# request para abrir e ler uma url


def read(url):
    with request.urlopen(url) as entrada:
        print('Baixando o CSV...')
        dados = entrada.read().decode('latin1')
        # decode('latin1') deve ser usado para decodificação dos
        # caracteres especiais+acentuação da lingua
        print('Download Completo!')
        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[8]}: {cidade[3]}')


if __name__ == '__main__':
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
    # read(r'.....), neste caso o "r" é usado para que caracteres especiais
    # possam ser usados e lidos como string para evitar erros do interpretador
