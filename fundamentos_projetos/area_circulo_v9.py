#!/usr/local/bin/python3
from math import pi

# adicionando return a função de forma aos dados de entrada e saída poderem ser usados e não somente impressos


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    raio = input('Informe o raio: ')  # retorno do input é uma string
    area = circulo(raio)
    print(area)
