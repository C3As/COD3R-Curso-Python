#!/usr/local/bin/python3
from math import pi

# criando uma função identificada como "circulo"


def circulo(raio):
    print('Área do círculo :', pi * float(raio) ** 2)


if __name__ == '__main__':
    raio = input('Informe o raio: ')  # retorno do input é uma string
    circulo(raio)
