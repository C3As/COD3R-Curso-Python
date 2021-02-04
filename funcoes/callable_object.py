#!/usr/local/bin/python3
class Potencia:
    # Calcula uma potencia especifica
    def __init__(self, expoente):  # construtor padrão
        # (self) está relacionada a própria instancia - param obrigatorio
        self.expoente = expoente

    def __call__(self, base):
        return base ** self.expoente


if __name__ == '__main__':
    quadrado = Potencia(2)
    cubo = Potencia(3)

    if callable(quadrado) and callable(cubo):
        print(f'3Q => {quadrado(3)}')
        print(f'5C => {cubo(5)}')
        print(Potencia(4)(2))  # 2 é a base 3 4 é a potencia
