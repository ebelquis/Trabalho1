from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, celular):
        super().__init__(nome, celular)
        self.__compras = []

    @property
    def compras(self):
        return self.__compras
    
    @compras.setter
    def compras(self, compras):
        self.__compras = compras
    
    #coloquei a mais
    def adicionar_compra(self, nova_compra):
        self.__compras.append(nova_compra)