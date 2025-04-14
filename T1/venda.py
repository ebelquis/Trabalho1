from datetime import datetime
from vendedor import Vendedor
from cliente import Cliente
from transacao import Transacao
from produto import Produto

class Venda(Transacao):
    def __init__(self, quantidade: int, produto: Produto, data: datetime, valor: float, cliente: Cliente, vendedor: Vendedor):
        super().__init__(quantidade, produto, data, valor)
        self.__cliente = cliente
        self.__vendedor = vendedor

#adicionar pedido automaticamente para o cliente?

    @property
    def cliente(self):
        return self.__cliente
    
    @cliente.setter
    def cliente(self, cliente: Cliente):
        self.__cliente = cliente
    
    @property
    def vendedor(self):
        return self.__vendedor
    
    @vendedor.setter
    def vendedor(self, vendedor: Vendedor):
        self.__vendedor = vendedor