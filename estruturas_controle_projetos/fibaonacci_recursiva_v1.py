#!/usr/local/bin/python3
def fibonacci(quantidade, sequencia=(0, 1)):
    # sequencia=(0,1) é uma tupla, que foi passada como parametro padrão;
    # que caso não seja passado será assumido.
    if len(sequencia) == quantidade:  # Importante: condição de parada
        return sequencia
    return fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))
    # tupla é imutável mas o retorno da função é uma nova tupla resultado da
    # soma da tupla parametro e a tupla da soma dos dois últimos elementos.


if __name__ == '__main__':
    # Listar os 20 primeiros números da sequencia
    for fib in fibonacci(20):
        print(fib, end=', ')
    print('')
