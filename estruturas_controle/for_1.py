for i in range(1, 11):
    print('i = {}'.format(i))

for j in range(10):  # subentende-se que o range começa no zero = range(0, 10)
    print(f'j = {j}')

for x in range(1, 11):
    for y in range(1, 11):
        print(f'{x} * {y} = {x * y}')
