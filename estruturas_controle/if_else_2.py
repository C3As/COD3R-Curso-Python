#!/usr/local/bin/python3
import sys

# uso de range , uso de tupla (17, 0, 35, 87, 113, -2)

def faixa_etaria(idade):
    if 0 <= idade < 18:
        return 'Menor de Idade'
    elif idade in range(18, 65): # 65 não faz parte
        return 'Adulto'
    elif idade in range(65, 100):
        return 'Melhor Idade'
    elif idade >= 100:
        return 'Centenário'
    else:
        return 'idade inválida'


if __name__ == '__main__':
    for idade in (17, 0, 35, 87, 113, -2):
        print(f'{idade}: {faixa_etaria(idade)}')
