#!/usr/local/bin/python3
from math import pi
import sys

# utilizando argumento passado na chamada do programa(./area_circulo_v10.py 12.4) utilizando import sys


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    # print(sys.argv[0]) # o primeiro argumento é o nome do arquivo - ./area_circulo_v10.py
    raio = sys.argv[1]
    area = circulo(raio)
    print(area)
