#!/usr/local/bin/python3
def fibonacci(sequencia=[0, 1]):
    # usando lista como parametro padrão, lista é mutável
    # Uso de mutáveis como valor default (armadilha)
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


if __name__ == '__main__':
    inicio = fibonacci()
    print(inicio, id(inicio))  # [0, 1, 1] 140706181369728
    print(fibonacci(inicio))  # [0, 1, 1, 2]
    restart = fibonacci()
    print(restart, id(restart))  # [0, 1, 1, 2, 3] 140706181369728
    # a lista mutável sequencia foi alterada desde a primeira chamada da função
    assert restart == [0, 1, 1]
