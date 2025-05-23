from entidade.produto import Produto
from entidade.endereco import Endereco

class Fornecedor:
    def __init__(self, nome: str, cnpj: int, celular: int, produto: Produto, preco: float):
        self.__nome = nome
        self.__cnpj = cnpj
        self.__celular = celular
        self.__produto = produto
        self.__preco = preco
        self.__enderecos = []

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
    
    @property
    def lista_enderecos(self):
        return self.__enderecos

    def incluir_endereco(self, cep = "", rua = "", numero = ""):
        self.__enderecos.append(Endereco(cep, rua, numero))

    def remover_endereco(self, cep):
        for endereco in self.__enderecos:
            if endereco.cep == cep:
                self.__enderecos.remove(endereco)
