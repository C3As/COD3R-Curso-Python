#!/usr/local/bin/python3

# gerador de codigo html com teste
def tag_bloco(texto, classe='sucess'):
    # classe='sucess' é um parametro padrão, ou seja, caso nada seja
    # passado na chamada da função este valor será assumido
    return f'<div class="{classe}">{texto}</div>'


if __name__ == '__main__':
    # Testes (asserions) - verifica uma determinada condição
    assert tag_bloco('Incluido com sucesso!') == \
        '<div class="sucess">Incluido com sucesso!</div>'
    # se a função estiver não estiver funcionando corretamente ocorrerá um
    # erro e uma msg será exibida
    assert tag_bloco('Impossível excluir!', 'error') == \
        '<div class="error">Impossível excluir!</div>'
    print(tag_bloco('bloco'))
