#!/usr/local/bin/python3

# gerador de codigo html
# com parametro nomeado não há necessidade de manter a ordem
def tag_bloco(texto, classe='sucess', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', 'info', True))
    print(tag_bloco('inline', inline=True))
    # inline=True - parametro nomeado
    print(tag_bloco('falhou', classe='error'))
    # classe='error' - parametro nomeado
