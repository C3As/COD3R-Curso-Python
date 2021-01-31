# o Exemplo abaixo simula a mesma funcionalidade do switch que existe em outras linguagens

def get_dia_semana(dia):
    dias = {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sabado'
    }
    return dias.get(dia, '** inválido **')
    # o segundo parametro da função get é o valor default que será retornado caso não sejá achado dentro do dicionário o valor procurado


if __name__ == '__main__':
    for dia in range(0, 9):
        print(f'{dia}: {get_dia_semana(dia)}')
