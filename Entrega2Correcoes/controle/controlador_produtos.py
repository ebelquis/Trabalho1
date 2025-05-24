from limite.tela_produto import TelaProduto
from entidade.produto import Produto

caneca = Produto("caneca", 1, 20.00, 10)
camisa = Produto('camisa m', 21, 40.00, 6)

class ControladorProdutos():
    def __init__(self, controlador_sistema):
        self.__produtos = [caneca, camisa]
        self.__controlador_sistema = controlador_sistema
        self.__tela_produto = TelaProduto()

    def pega_produto_por_codigo(self, codigo: int):
        for produto in self.__produtos:
            if produto.codigo == codigo:
                return produto
        return None

    def incluir_produto(self):
        dados_produto = self.__tela_produto.pega_dados_produto()
        codigo = self.pega_produto_por_codigo(int(dados_produto["codigo"]))
        if codigo is None:
            produto = Produto(dados_produto["nome"], 
                              dados_produto["codigo"],
                              float(dados_produto["preco_venda"]),
                              int(dados_produto["quant_estoque"]))
            self.__produtos.append(produto)
            self._tela_produto.mostra_mensagem("Produto incluído com sucesso!")
        else:
            self.__tela_produto.mostra_mensagem("ATENÇÃO: Produto já existente")

    def alterar_preco_produto(self):
        self.lista_produtos()
        codigo = int(self.__tela_produto.seleciona_produto())
        produto = self.pega_produto_por_codigo(codigo)
        if produto is not None:
            produto.preco_venda = float(self.__tela_produto.pega_preco())
            self.__tela_produto.mostra_mensagem("Preço do produto alterado com sucesso!")
            self.lista_produtos()
        else:
            self.__tela_produto.mostra_mensagem("ATENÇÃO: Produto não existente")

    def alterar_estoque(self):
        self.lista_produtos()
        codigo_produto = self.__tela_produto.seleciona_produto()
        produto = self.pega_produto_por_codigo(codigo_produto)

        if produto is not None:
            produto.quant_estoque = int(self.__tela_produto.pega_quantidade()) 
            self.lista_produtos()

    def lista_produtos(self):
        if not self.__produtos:
            self.__tela_produto.mostra_mensagem("Não há produtos cadastrados.")
            return None

        for produto in self.__produtos:
            self.__tela_produto.mostra_produto({"nome": produto.nome,
                                              "codigo": produto.codigo_produto,
                                              "preco_venda": produto.preco_venda,
                                              "quant_estoque": produto.quant_estoque})

    def excluir_produto(self):
        self.lista_produtos()
        codigo_produto = int(self.__tela_produto.seleciona_produto())
        produto = self.pega_produto_por_codigo(codigo_produto)
        if produto is not None:
            self.__produtos.remove(produto)
            self.__tela_produto.mostra_mensagem("Produto excluído com sucesso!")
            self.lista_produtos()
        else:
            self.__tela_produto.mostra_mensagem("ATENÇÃO: Produto não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_produto,
                        2: self.alterar_preco_produto,
                        3: self.alterar_estoque,
                        4: self.lista_produtos,
                        5: self.excluir_produto,
                        0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_produto.tela_opcoes()
            if opcao_escolhida in lista_opcoes:
                lista_opcoes[opcao_escolhida]()
            else:
                self.__tela_pedido.mostra_mensagem("Opção inválida, digite novamente.")