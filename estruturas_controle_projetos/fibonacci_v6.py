#!/usr/local/bin/python3
# 0,1,1,2,3,5,8,13,21  => seq. fibonacci o proximo numero será sempre a soma
# dos dois últimos

def fibonacci(quantidade):
    resultado = [0, 1]
    for i in range(2, quantidade):
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == '__main__':
    for fib in fibonacci(20):
        print(fib, end=', ')
