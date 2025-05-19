class Produto:
    def __init__(self, nome: str, codigo: int, preco_venda: float, quant_estoque: int):
        self.__nome = nome
        self.__codigo = codigo
        self.__preco_venda = preco_venda
        self.__quant_estoque = quant_estoque
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome
    
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo: str):
        self.__codigo = codigo
    
    @property
    def preco_venda(self):
        return self.__preco_venda
    
    @preco_venda.setter
    def preco_venda(self, preco_venda: float):
        self.__preco_venda = preco_venda
    
    @property
    def quant_estoque(self):
        return self.__quant_estoque
    
    @quant_estoque.setter
    def quant_estoque(self, quant_estoque: int):
        self.__quant_estoque = quant_estoque