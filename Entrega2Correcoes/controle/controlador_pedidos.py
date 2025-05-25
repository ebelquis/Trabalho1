<<<<<<< HEAD
from limite.tela_produto import TelaProduto
from entidade.produto import Produto

=======
from limite.tela_pedido import TelaPedido
from entidade.pedido import Pedido
from datetime import datetime
>>>>>>> bb35d15247fd653159199aa5c0d51242b2e10cbe

class ControladorPedidos():
    def __init__(self, controlador_sistema):
        self.__produtos = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_produto = TelaProduto()

<<<<<<< HEAD
    def pega_produto_por_codigo_produto(self, codigo_produto: int):
        for i in self.__produtos:
            if i.codigo_produto == codigo_produto:
                return i
        return None

    def incluir_produto(self):
        dados_produto = self.__tela_produto.pega_dados_produto()
        codigo_produto = self.pega_produto_por_codigo_produto(dados_produto["codigo_produto"])
        if codigo_produto is None:
            produto = Produto(dados_produto["nome"], 
                              dados_produto["codigo_produto"],
                              dados_produto["preco_venda"],
                              dados_produto["quant_estoque"])
            self.__produtos.append(produto)
=======
    def pega_pedido_por_codigo(self, codigo: str):
        for pedido in self.__pedidos:
            if(pedido.codigo == int(codigo)):
                return pedido
        return None

    def incluir_pedido(self):
        self.__controlador_sistema.controlador_fornecedores.lista_fornecedores()
        self.__controlador_sistema.controlador_produtos.lista_produtos()
        dados_pedido = self.__tela_pedido.pega_dados_pedido()

        cnpj = dados_pedido["cnpj"]
        codigo_pedido = int(dados_pedido["codigo"])
        codigo_produto = int(dados_pedido["codigo_produto"])
        quantidade = int(dados_pedido["quantidade"])
        data = dados_pedido["data"]
        frete = float(dados_pedido["valor_frete"])
        prazo = int(dados_pedido["prazo_entrega"])

        fornecedor = self.__controlador_sistema.controlador_fornecedores.pega_fornecedor_por_cnpj(cnpj)
        produto = self.__controlador_sistema.controlador_produtos.pega_produto_por_codigo(codigo_produto)

        if (fornecedor is not None and produto is not None):
            pedido_existente = self.pega_pedido_por_codigo(str(codigo_pedido))
            valor_pedido = produto.preco_venda * quantidade
            if pedido_existente is None:
                pedido = Pedido(quantidade, produto, data,
                                valor_pedido, fornecedor, frete, prazo)
                self.__controlador_sistema.controlador_produtos.aumenta_quantidade_estoque(produto, quantidade)
                self.__pedidos.append(pedido)
                self.__tela_pedido.mostra_mensagem("Pedido incluído com sucesso!")
            else:
                self.__tela_pedido.mostra_mensagem("ATENÇÃO: Já existe um pedido com este código.")
>>>>>>> bb35d15247fd653159199aa5c0d51242b2e10cbe
        else:
            self.__tela_produto.mostra_mensagem("ATENCAO: Produto já existente")

<<<<<<< HEAD
    def alterar_preco_produto(self):
        self.lista_produtos()
        codigo_produto = self.__tela_produto.seleciona_produto()
        produto = self.pega_produto_por_codigo_produto(codigo_produto)
        if produto is not None:
            valor = self.__tela_produto.pega_dados_produto_alterar()
            produto.preco_venda = int(produto.preco_venda) + int(valor)
        else:
            self.__tela_produto.mostra_mensagem("ATENCAO: Produto não existente")

    def alterar_estoque(self):
        self.lista_produtos()
        codigo_produto_produto = self.__tela_produto.seleciona_produto()
        produto = self.pega_produto_por_codigo_produto(codigo_produto_produto)
        if produto is not None:
            valor = self.__tela_produto.pega_dados_produto_alterar()
            produto.quant_estoque = int(produto.quant_estoque) + int(valor) 
            self.lista_produtos()

    def lista_produtos(self):
        for produto in self.__produtos:
            self.__tela_produto.mostra_produto({"nome": produto.nome,
                                              "codigo_produto": produto.codigo_produto,
                                              "preco_venda": produto.preco_venda,
                                              "quant_estoque": produto.quant_estoque})

    def excluir_produto(self):
        self.lista_produtos()
        codigo_produto_produto = self.__tela_produto.seleciona_produto()
        produto = self.pega_produto_por_codigo_produto(codigo_produto_produto)
        if produto is not None:
            self.__produtos.remove(produto)
        else:
            self.__tela_produto.mostra_mensagem("ATENCAO: Produto não existente")
=======
    def lista_pedido(self):
        if not self.__pedidos:
            self.__tela_pedido.mostra_mensagem("Não há pedidos cadastrados.")
            return None
        for pedido in self.__pedidos:
            self.__tela_pedido.mostra_pedido({"codigo": pedido.codigo,
                                              "quantidade": pedido.quantidade,
                                              "produto": pedido.produto.nome,
                                              "data": pedido.data,
                                              "valor": pedido.valor,
                                              "frete": pedido.frete,
                                              "prazo_entrega": pedido.prazo_entrega})
    
    def excluir_pedido(self):
        self.lista_pedido()
        codigo_pedido = self.__tela_pedido.seleciona_pedido()
        pedido = self.pega_pedido_por_codigo(codigo_pedido)
        quantidade = -1 * (int(pedido.quantidade))

        if (pedido is not None):
            self.__controlador_sistema.controlador_produtos.aumenta_quantidade_estoque(pedido, quantidade)
            self.__pedidos.remove(pedido)
            self.__tela_pedido.mostra_mensagem("Pedido excluído com sucesso!")
            self.lista_pedido()
        else:
            self.__tela_venda.mostra_mensagem("ATEÇÃO: Pedido não existente")
>>>>>>> bb35d15247fd653159199aa5c0d51242b2e10cbe

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
<<<<<<< HEAD
            opcao = self.__tela_produto.tela_opcoes()
            if opcao in lista_opcoes:
                lista_opcoes[opcao]()
=======
            opcao_escolhida = self.__tela_pedido.tela_opcoes()
            if opcao_escolhida in lista_opcoes:
                lista_opcoes[opcao_escolhida]()
            else:
                self.__tela_pedido.mostra_mensagem("Opção inválida, digite novamente.")
>>>>>>> bb35d15247fd653159199aa5c0d51242b2e10cbe
