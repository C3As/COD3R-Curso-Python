# **kwargs => key words args
def resultado_f1(**podium):
    # gerará um dicionário : chave&valor
    for posicao, piloto in podium.items():
        print(f'{posicao} -> {piloto}')


if __name__ == '__main__':
    resultado_f1(primeiro='L.Hamilton',
                 segundo='M. Verstappen',
                 terceiro='S. Vettel')
