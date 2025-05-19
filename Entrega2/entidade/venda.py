from datetime import datetime
from entidade.vendedor import Vendedor
from entidade.cliente import Cliente
from entidade.transacao import Transacao
from entidade.produto import Produto

class Venda(Transacao):
    def __init__(self, quantidade: int, produto: Produto, data: datetime, valor: float, codigo: int, cliente: Cliente, vendedor: Vendedor):
        super().__init__(quantidade, produto, data, valor, codigo)
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