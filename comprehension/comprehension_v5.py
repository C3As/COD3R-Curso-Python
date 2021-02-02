# { chave: valor/expressao for item in list if condicional }

dicionario = {i: i * 2 for i in range(10) if i % 2 == 0}
print(dicionario)  # {0: 0, 2: 4, 4: 8, 6: 12, 8: 16}

for numero, dobro in dicionario.items():
    print(f'{numero} x 2 = {dobro}')
