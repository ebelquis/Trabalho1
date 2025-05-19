from excessoes.OpcaoErroException import OpcaoErroException

class TelaSistema:
    def tela_opcoes(self):
        print("-------- SISTEMA DE ESTOQUE DA A5 ---------")
        print("Escolha sua opcao")
        print("1 - Venda feita pelo Vendedor")
        print("2 - Fornecedor")
        print("3 - Produto")
        print("4 - Pessoa")
        print("5 - Pedido feito para o fornecedor")
        print("0 - Finalizar sistema")

        try:
            opcao = int(input("Escolha a opcao: "))
            if opcao not in [0, 1, 2, 3, 4, 5]:
                raise OpcaoErroException()
            return opcao
        except OpcaoErroException as e:
            self.__tela_venda.mostra_mensagem(e)