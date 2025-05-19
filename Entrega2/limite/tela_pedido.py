from datetime import datetime
from excessoes.OpcaoErroException import OpcaoErroException


class TelaPedido():
    def tela_opcoes(self):
        print("-------- PEDIDOS ----------")
        print("Escolha a opcao")
        print("1 - Fazer Pedido")
        print("2 - Listar Pedido")
        print("3 - Excluir Pedido")
        print("0 - Retornar")

        try:
            opcao = int(input("Escolha a opcao: "))
            if opcao not in [0, 1, 2, 3]:
                raise OpcaoErroException()
            return opcao
        except OpcaoErroException as e:
            self.mostra_mensagem(e)

    def pega_dados_(self):
        print("-------- DADOS PEDIDOS ----------")
        while True:
            try:
                cnpj = int(input("CNPJ do fornecedor: "))
                break
            except ValueError:
                print("cnpj inválido. Insira um valor valido.")

        while True:
            try:
                codigo = int(input("Codigo do pedido: "))
                break
            except ValueError:
                print("codigo inválido. Insira um valor valido. (erro de digitacao)")

        while True:
            try:
                codigo_produto = int(input("Codigo do produto: "))
                break
            except ValueError:
                print("codigo inválido. Insira um valor valido (erro de digitacao).")

        while True:
            try:
                quantidade = int(input("Quantidade do pedido:  "))
                break
            except ValueError:
                print("quantidade inválida. Insira um valor valido (erro de digitacao).")

        while True:
            try:
                data = input("Data do pedido (exemplo de entrada: 29/08/2005): ")
                data = datetime.strptime(data, "%d/%m/%Y")  
                break
            except ValueError:
                print("Data inválida. Insira a data no formato (dd/mm/yyyy).")

        while True:
            try:
                valor_frete = int(input("Valor do frete do pedido: "))
                break
            except ValueError:
                print("insira um valor valido (erro de digitacao).")

        while True:
            try:
                prazo_entrega = int(input("prazo do pedido (exemplo de entrada: 14): "))
                break
            except ValueError:
                print("Prazo inválido. Insira o prazo certo (erro de digitacao)!")

        return {"cnpj": cnpj, "codigo": codigo,
                "codigo_produto": codigo_produto,
                "quantidade": quantidade,
                "data": data,
                "valor_frete": valor_frete,
                "prazo_entrega": prazo_entrega}
    

    def mostra_pedidos(self, dados_pedidos):
        print("CODIGO DO PEDIDO: ", dados_pedidos["codigo"])
        print("QUANTIDADE DO PEDIDO: ", dados_pedidos["quantidade"])
        print("NOME DO PRODUTO: ", dados_pedidos["nome_produto"])
        print("DATA DO PEDIDO: ", dados_pedidos["data"])
        print("VALOR DO PRODUTO: ", dados_pedidos["valor"])
        print("NOME DO FORNECEDOR: ", dados_pedidos["nome_fornecedor"])
        print("VALOR DO FRETE: ", dados_pedidos["frete"])
        print("PRAZO DE ENTREGA: ", dados_pedidos["prazo_entrega"])
        print("\n")

    def seleciona_pedido(self):
        while True:
            try:
                codigo = int(input("Código do pedido que deseja selecionar: "))
                break
            except ValueError:
                print("digite um valor valido (erro de digitacao)")
            return codigo

    def mostra_mensagem(self, msg):
        print(msg)