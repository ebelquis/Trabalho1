from limite.tela_venda import TelaVenda
from entidade.venda import Venda

class ControladorVendas():

  def __init__(self, controlador_sistema):
    self.__controlador_sistema = controlador_sistema
    self.__vendas = []
    self.__tela_venda = TelaVenda()

  def pega_venda_por_codigo(self, codigo: int):
    for venda in self.__vendas:
      if(venda.codigo == codigo):
        return venda
    return None

  def incluir_venda(self):
    self.__controlador_sistema.controlador_pessoas.lista_cliente()
    self.__controlador_sistema.controlador_pessoas.lista_vendedores()
    dados_venda = self.__tela_venda.pega_dados_venda()

    cliente = self.__controlador_sistema.controlador_pessoas.pega_cliente_por_cpf(dados_venda["cpf_cliente"])
    vendedor = self.__controlador_sistema.controlador_pessoas.pega_vendedor_por_cpf(dados_venda["cpf_vendedor"])
    produto = self.__controlador_sistema.controlador_produto.pega_produto_por_codigo(dados_venda["codigo_produto"])

    if (cliente is not None and vendedor is not None and produto is not None):
      valor_total = produto.preco_venda * dados_venda["quantidade"]
      venda = Venda(dados_venda["quantidade"], produto,
                    dados_venda["data"], valor_total, dados_venda["codigo"],
                    cliente, vendedor)
            
      vendedor.valor_vendido_total += valor_total
      self.__vendas.append(venda)
      produto.quant_estoque -= dados_venda["quantidade"]

    else:
      self.__tela_venda.mostra_mensagem("Dados inválidos")

  def lista_venda(self):
    for venda in self.__vendas:
      self.__tela_venda.mostra_venda({"codigo": venda.codigo,
                                      "vendedor": venda.vendedor.nome,
                                      "cliente": venda.cliente.nome,
                                      "produto": venda.produto.valor,
                                      "data": venda.data,
                                      "valor": venda.valor_total})
    
  def excluir_venda(self):
    self.lista_venda()
    codigo_venda = self.__tela_venda.seleciona_venda()
    venda = self.pega_venda_por_codigo(codigo_venda)

    if (venda is not None):
      venda.vendedor.valor_vendido_total -= venda.valor
      venda.produto.quant_estoque += venda.quantidade
      self.__vendas.remove(venda)
      self.lista_venda()

    else:
      self.__tela_venda.mostra_mensagem("ATENCAO: Venda não existente")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_venda,
                    2: self.lista_venda,
                    3: self.excluir_venda,
                    0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_venda.tela_opcoes()]()