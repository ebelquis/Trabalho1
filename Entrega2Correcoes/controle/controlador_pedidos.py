from limite.tela_pedido import TelaPedido
from entidade.pedido import Pedido
from datetime import datetime

class ControladorPedidos():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__pedidos = []
        self.__tela_pedido = TelaPedido()

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
        else:
            self.__tela_pedido.mostra_mensagem("Dados inválidos")

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

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_pedido,
            2: self.lista_pedido,
            3: self.excluir_pedido,
            0: self.retornar
        }

        continua = True
        while continua:
            opcao_escolhida = self.__tela_pedido.tela_opcoes()
            if opcao_escolhida in lista_opcoes:
                lista_opcoes[opcao_escolhida]()
            else:
                self.__tela_pedido.mostra_mensagem("Opção inválida, digite novamente.")
