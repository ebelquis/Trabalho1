class Produto:
    def __init__(self, nome: str, descricao: str, preco_venda: float, quant_estoque: int):
        self.__nome = nome
        self.__descricao = descricao
        self.__preco_venda = preco_venda
        self.__quant_estoque = quant_estoque
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome
    
    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao
    
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