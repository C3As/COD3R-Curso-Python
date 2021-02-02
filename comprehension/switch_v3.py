def get_tipo_dia(dia):
    dias = {
        (1, 7): 'Fim de Semana',
        # uma tupla com valores de 1 e 7 que são chaves do dicionário dias
        tuple(range(2, 7)): 'Dia da Semana',
        # outra tupla com valores dentro do range de 2 a 6 tb chaves
    }
    # equivale a:
    # dias = {
    #     1: 'Fim de semana',
    #     2: 'Dia de semana',
    #     3: 'Dia de semana',
    #     4: 'Dia de semana',
    #     5: 'Dia de semana',
    #     6: 'Dia de semana',
    #     7: 'Fim de semana'
    # }
    dia_escolhido = (tipo for numeros, tipo in dias.items() if dia in numeros)
    return next(dia_escolhido, '** dia inválido **')
    # expressão for item in list if condicional
    # como é um dicionario item = chave & valor = numeros e tipo


if __name__ == '__main__':
    for dia in range(0, 9):
        print(f'{dia}: {get_tipo_dia(dia)}')
