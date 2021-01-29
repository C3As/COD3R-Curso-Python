#!/usr/local/bin/python3
from math import pi
import sys

# validando os dados dos argumentos passados


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:  # verifica se o segundo argumento foi passado na chamada do programa
        print("É necessário informar o raio do círculo.")
        print("Sintaxe: " + sys.argv[0][2:] + " <raio>")
        # """ significa que tudo que for usado entre as aspas triplas será impresso
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print(area)
