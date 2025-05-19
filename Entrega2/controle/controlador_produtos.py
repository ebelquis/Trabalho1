from limite.tela_produto import TelaProduto
from entidade.produto import Produto

class ControladorProdutos():
    def __init__(self, controlador_sistema):
        self.__produtos = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_produto = TelaProduto()

    def pega_produto_por_codigo(self, codigo: str):
        for produto in self.__produtos:
            if produto.codigo == codigo:
                return produto
        return None

    def incluir_produto(self):
        dados_produto = self.__tela_produto.pega_dados_produto()
        codigo = self.pega_produto_por_codigo(dados_produto["codigo"])
        if codigo is None:
            produto = Produto(dados_produto["nome"], 
                              dados_produto["codigo"],
                              dados_produto["preco_venda"],
                              dados_produto["quant_estoque"])
            self.__produtos.append(produto)
        else:
            self.__tela_produto.mostra_mensagem("ATENCAO: Produto já existente")

    def alterar_preco_produto(self):
        self.lista_produtos()
        codigo_produto = self.__tela_produto.seleciona_produto()
        produto = self.pega_produto_por_codigo(codigo_produto)
        if produto is not None:
            novos_dados_produto = self.__tela_produto.pega_dados_produto_alterar()
            produto.preco_venda += int(novos_dados_produto["valor"])
            self.lista_produtos()
        else:
            self.__tela_produto.mostra_mensagem("ATENCAO: Produto não existente")

    def alterar_estoque(self):
        self.lista_produtos()
        codigo_produto = self.__tela_produto.seleciona_produto()
        produto = self.pega_produto_por_codigo(codigo_produto)
        if produto is not None:
            novos_dados_produto = self.__tela_produto.pega_dados_produto_alterar()
            produto.quant_estoque += int(novos_dados_produto["valor"]) 
            self.lista_produtos()

    def lista_produtos(self):
        for produto in self.__produtos:
            self.__tela_produto.mostra_produto({"nome": produto.nome,
                                              "codigo": produto.codigo,
                                              "preco_venda": produto.preco_venda,
                                              "quant_estoque": produto.quant_estoque})

    def excluir_produto(self):
        self.lista_produtos()
        codigo_produto = self.__tela_produto.seleciona_produto()
        produto = self.pega_produto_por_codigo(codigo_produto)
        if produto is not None:
            self.__produtos.remove(produto)
            self.lista_produtos()
        else:
            self.__tela_produto.mostra_mensagem("ATENCAO: Produto não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_produto,
                        2: self.alterar_preco_produto,
                        3: self.alterar_estoque,
                        4: self.lista_produtos,
                        5: self.excluir_produto,
                        0: self.retornar}

        continua = True
        while continua:
            opcao = self.__tela_produto.tela_opcoes()
            if opcao in lista_opcoes:
                lista_opcoes[opcao]()