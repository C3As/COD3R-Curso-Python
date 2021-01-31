def imprimir(maximo, atual):
    if atual >= maximo:  # condicao de parada
        return
    print(atual, end=', ')
    imprimir(maximo, atual+1)


imprimir(10, 1)
print('')
