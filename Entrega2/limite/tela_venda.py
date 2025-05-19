from datetime import datetime
from excessoes.OpcaoErroException import OpcaoErroException

class TelaVenda():
    def tela_opcoes(self):
        print("-------- PEDIDOS ----------")
        print("Escolha a opcao")
        print("1 - Fazer Venda")
        print("2 - Listar Venda")
        print("3 - Excluir Venda")
        print("0 - Retornar")
        
        try:
            opcao = int(input("Escolha a opcao: "))
            if opcao not in [0, 1, 2, 3]:
                raise OpcaoErroException()
            return opcao
        except OpcaoErroException as e:
            self.__tela_venda.mostra_mensagem(e)

    def pega_dados(self):
        print("-------- DADOS VENDA ----------")
        while True:
            try:
                cpf_vendedor = int(input("Cpf do vendedor: "))
                break
            except ValueError:
                print("cpf inválido. Insira um valor válido (somente numeros) (erro na digitacao)..")

        while True:
            try:
                cpf_cliente = int(input("Cpf do cliente: "))
                break
            except ValueError:
                print("cpf inválido. Insira um valor válido (somente numeros) (erro na digitacao)..")

        while True:
            try:
                quantidade = int(input("Quantidade vendida: "))
                break
            except ValueError:
                print("Quantidade inválida. Insira valor válido (somente numeros) (erro na digitacao).")

        while True:
            try:
                data = input("Data da venda (exemplo de entrada: 29/08/2005): ")
                data = datetime.strptime(data, "%d/%m/%Y")  
                break
            except ValueError:
                print("Data inválida. Insira a data no formato (dd/mm/yyyy) (erro na digitacao)..")

        while True:
            try:
                codigo_produto = int(input("Código do produto: "))
                break
            except ValueError:
                print("Código inválido. Insira um valor válido (erro na digitacao)..")

        while True:
            try:
                codigo = int(input("Código da venda: "))
                break
            except ValueError:
                print("Código inválido. Insira um codigo válido (erro na digitacao)..")

        return {"cpf_vendedor": cpf_vendedor,
                "cpf_cliente": cpf_cliente,
                "quantidade": quantidade,
                "data": data,
                "codigo_produto": codigo_produto,
                "codigo": codigo
                }


    def mostra_pedidos(self, dados_venda):
        print("CODIGO DA VENDA: ", dados_venda["codigo"])
        print("VENDEDOR: ", dados_venda["vendedor"])
        print("CLIENTE: ", dados_venda["cliente"])
        print("NOME DO PRODUTO: ", dados_venda["produto"])
        print("DATA DA VENDA: ", dados_venda["data"])
        print("VALOR DA VENDA: ", dados_venda["valor"])
        print("\n")

    def seleciona_pedido(self):
        while True:
            try:
                codigo = int(input("Código da venda que deseja selecionar: "))
                break
            except ValueError:
                print("O seu codigo esta errado (erro na digitacao).")
        return codigo

    def mostra_mensagem(self, msg):
        print(msg)