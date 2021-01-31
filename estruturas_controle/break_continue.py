for x in range(1, 11):
    if x % 2 == 0:
        continue  # interrompe prematuramente a iteração indo diretamente para a próxima iteração mas ainda dentro do laço "for"
    print(x)

for x in range(1, 11):
    if x == 5:
        break  # para completamente a iteração saindo do laço "for" executando os códigos fora do laço
    print(x)
print('Fim!')
