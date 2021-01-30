palavra = 'paralelepípedo'  # percorrendo uma string
for letra in palavra:
    print(letra, end=', ')
    # incluindo end=','significa que o final de cada print será a virgula, \n é o padrão
print(' Fim')

aprovados = ['Rafaela', 'Pedro', 'Renato', 'Maria']  # percorrendo uma lista
for nome in aprovados:
    print(nome, end=', ')
print(' Fim')

for posicao, nome in enumerate(aprovados):
    # The enumerate object yields pairs containing a count (from start, which defaults to zero) and a value yielded by the iterable argument.
    print(f'{posicao + 1})', nome)

dias_semana = ('Domingo', 'Segunda', 'Terça',
               'Quarta', 'Quinta', 'Sexta', 'Sábado')  # percorrendo uma tupla
for dia in dias_semana:
    print(f'Hoje é {dia}')

for letra in set('muito legal'):  # percorrendo uma lista
    print(letra)
