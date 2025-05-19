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
        opcao = int(input("Escolha a opcao:"))
        return opcao
