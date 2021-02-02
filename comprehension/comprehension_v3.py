generator = (i ** 2 for i in range(10) if i % 2 == 0)
print(next(generator))  # Saida 0
print(next(generator))  # Saida 4
print(next(generator))  # Saida 16
print(next(generator))  # Saida 36
print(next(generator))  # Saida 64


# generator funciona da mesma forma do que list comprehensio, mas:
#   1) usa parenteses ao inves de colchetes
#   2) não gera a lista toda ao mesmo tempo
#   3) gera elementos por demanda
#   4) reduz a necessidade de memória desta forma
