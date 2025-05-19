#daria para colocar como classe filha de Pessoa
#from pessoa import Pessoa
from produto import Produto

class Fornecedor:
    def __init__(self, nome: str, cnpj: int, celular: int, produto: Produto, preco: float):
        self.__nome = nome
        self.__cnpj = cnpj
        self.__celular = celular
        self.__produto = produto
        self.__preco = preco
    
    @property
    def cnpj(self) -> int:
        return self.__cnpj
    
    @cnpj.setter
    def cnpj(self, cnpj: int):
        self.__cnpj = cnpj
    
    @property
    def produto(self) -> Produto:
        return self.__produto
    
    @produto.setter
    def produto(self, produto: Produto):
        self.__produto = produto
    
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, preco: float):
        self.__preco = preco
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def celular(self):
        return self.__celular
    
    @celular.setter
    def celular(self, celular):
        self.__celular = celular