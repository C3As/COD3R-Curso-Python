# função chamando outra função
def executar(funcao):
    if callable(funcao):
        # verifica se o parametro passado é possível de chamado como funcao
        funcao()


def bom_dia():
    print('Bom Dia!')


def boa_tarde():
    print('Boa Tarde!')


if __name__ == '__main__':
    executar(bom_dia)
    executar(boa_tarde)
    executar(1)  # 1 não é uma função - funcao executar testa se é um callable
