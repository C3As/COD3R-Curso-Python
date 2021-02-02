# List_comprehension oferece uma sintaxe mais curta quando
# você deseja criar uma nova lista com base nos valores de um lista existente.

# [ expressão for item in list if condicional]

dobros = [i * 2 for i in range(10)]
# if condicional não foram usados p/exemplo acima
print(dobros)


# Versaão 'normal'
dobros = []
for i in range(10):
    dobros.append(i*2)
print(dobros)
