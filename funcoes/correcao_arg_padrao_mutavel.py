#!/usr/local/bin/python3
def fibonacci(sequencia=None):
    sequencia = sequencia or [0, 1]
    # se sequencia for none assumitra [0, 1]
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


if __name__ == '__main__':
    inicio = fibonacci()
    print(inicio, id(inicio))  # [0, 1, 1] 140706181369728
    print(fibonacci(inicio))  # [0, 1, 1, 2]
    restart = fibonacci()
    print(restart, id(restart))  # [0, 1, 1] 140410550483840
    # ao se reiniciar a função o valor padrao será none reiniciando a sequencia
    assert restart == [0, 1, 1]
