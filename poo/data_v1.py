class Data:
    def __init__(self, dia, mes, ano):  # construtor padrão do objeto
        self.dia = dia  # inicializando variáveis
        self.mes = mes
        self.ano = ano

    def __str__(self):  # self é o objeto que está em execução
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data(5, 12, 2019)
# d1.dia = 5
# d1.mes = 12
# d1.ano = 2019
print(d1)

d2 = Data(15, 10, 1963)
# d2.dia = 15
# d2.mes = 10
# d2.ano = 1963
print(d2)
