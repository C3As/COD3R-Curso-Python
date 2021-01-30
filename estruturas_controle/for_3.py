produto = {'nome': 'Caneta Chic', 'preco': 14.99,
           'importada': True, 'estoque': 793}  # percorrendo um dicionario(chave e valor)
for chave in produto:  # por padrão percorre a chave - pode ser escrito produto.keys()
    print(chave)

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(chave, '=', valor)

