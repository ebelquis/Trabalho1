from limite.tela_pedido import TelaPedido
from entidade.pedido import Pedido

class ControladorPedidos():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__pedidos = []
        self.__tela_pedido = TelaPedido()

    def pega_pedido_por_codigo(self, codigo: int):
        for pedido in self.__pedidos:
            if(pedido.codigo == codigo):
                return pedido
        return None

    def incluir_pedido(self):
        self.__controlador_sistema.controlador_fornecedores.lista_fornecedores()
        self.__controlador_sistema.controlador_produtos.lista_produtos()
        dados_pedido = self.__tela_pedido.pega_dados_pedido()

        fornecedor = self.__controlador_sistema.controlador_fornecedores.pega_fornecedor_por_cnpj(dados_pedido["cnpj"])
        produto = self.__controlador_sistema.controlador_produtos.pega_produto_por_codigo(dados_pedido["codigo_produto"])

        if (fornecedor is not None and produto is not None):
            pedido = Pedido(dados_pedido["quantidade"], produto,
                           dados_pedido["data"], (produto.preco_venda * dados_pedido["quantidade"]), 
                           fornecedor, dados_pedido["frete"], dados_pedido["prazo_entrega"])
            
            self.__controlador_sistema.controlador_produtos.aumenta_quantidade_estoque(produto, dados_pedido["quantidade"])
            self.__pedidos.append(pedido)
        else:
            self.__tela_pedido.mostra_mensagem("Dados inválidos")

    def lista_pedido(self):
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
            self.lista_pedido()
        else:
            self.__tela_venda.mostra_mensagem("ATENCAO: Pedido não existente")

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
            lista_opcoes[self.__tela_pedido.tela_opcoes()]()