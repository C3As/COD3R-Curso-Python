# laço infinito - CUIDADO
# while True:
#      print('vai demorar muitooooo')

from random import randint
# randint(a: int, b: int) -> int
# Return random integer in range [a, b], including both end points.

numero_informado = -1
numero_secreto = randint(0, 9)

while numero_informado != numero_secreto:
    numero_informado = int(input('Informe o número: '))

print('Número secreto {} foi encontrado!'.format(numero_secreto))
