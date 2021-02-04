def todos_params(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')

# *args são os argumentos pocionais
# **kwargs são os argumentos nomeados


if __name__ == '__main__':
    todos_params('a', 'b', 'c')  # args: ('a', 'b', 'c') kwargs: {}
    todos_params(1, 2, 3, legal=True, valor=12.99)
    # args: (1, 2, 3)kwargs: {'legal': True, 'valor': 12.99}
    todos_params('Ana', False, [1, 2, 3], tamanho='M', fragil=False)
    # args: ('Ana', False, [1, 2, 3]) kwargs: {'tamanho': 'M', 'fragil': False}
    # todos_params(primeiro='João', 'Maria')
    # ERRO - positional argument follows keyword argument
    # no codigo da função os argumentos nomeados vem depois dos posionais
    # chamando-os invertidamente causará erro
