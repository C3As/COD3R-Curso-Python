class Carro:
    def __init__(self, vel_max):  # construtor padrão do objeto
        self.vel_max = vel_max
        self.vel_atual = 0

    def acelerar(self, delta=5):
        maxima = self.vel_max
        nova = self.vel_atual + delta
        self.vel_atual = nova if nova <= maxima else maxima
        return self.vel_atual

    def frear(self, delta=5):
        nova = self.vel_atual - delta
        self.vel_atual = nova if nova >= 0 else 0
        return self.vel_atual


if __name__ == '__main__':
    c1 = Carro(180)

    for i in range(25):
        print(c1.acelerar(8))

    for i in range(10):
        print(c1.frear(delta=20))
