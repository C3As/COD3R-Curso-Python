#!/usr/local/bin/python3
from math import pi
import sys

# melhorando o mensagem de erro mudando-o para função especifica


def circulo(raio):
    return pi * float(raio) ** 2


def help():
    print("É necessário informar o raio do círculo.")
    print("Sintaxe: " + sys.argv[0][2:] + " <raio>")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print(area)
