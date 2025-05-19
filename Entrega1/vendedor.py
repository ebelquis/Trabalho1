from pessoa import Pessoa

class Vendedor(Pessoa):
    def __init__(self, nome, celular, valor_vendido_total):
        super().__init__(nome, celular)
        self.__valor_vendido_total = valor_vendido_total

    @property
    def valor_vendido_total(self):
        return self.__valor_vendido_total

    @valor_vendido_total.setter
    def valor_vendido_total(self, valor_vendido_total):
        self.__valor_vendido_total = valor_vendido_total