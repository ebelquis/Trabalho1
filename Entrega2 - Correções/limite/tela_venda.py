class TelaVenda():
    def tela_opcoes(self):
        print("-------- VENDAS ----------")
        print("Escolha a opcao")
        print("1 - Fazer Venda")
        print("2 - Listar Venda")
        print("3 - Excluir Venda")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_venda(self):
        print("-------- DADOS VENDA ----------")
        cpf_vendedor = input("Cpf do vendedor: ")
        cpf_cliente = input("Cpf do cliente: ")
        quantidade = input("Quantidade vendida: ")
        valor = input("Valor da venda: ")
        data = input("Data da venda: ")
        codigo_produto = input("Codigo do produto: ")
        codigo = input("Codigo da venda: ")

        return {"cpf_vendedor": cpf_vendedor, 
                "cpf_cliente":cpf_cliente,
                "quantidade": quantidade,
                "valor": valor,
                "data": data,
                "codigo_produto": codigo_produto,
                "codigo": codigo}

    def mostra_venda(self, dados_venda):
        print("CODIGO DA VENDA: ", dados_venda["codigo"])
        print("VENDEDOR: ", dados_venda["vendedor"])
        print("CLIENTE: ", dados_venda["cliente"])
        print("NOME DO PRODUTO: ", dados_venda["produto"])
        print("QUANTIDADE: ", dados_venda["quantidade"])
        print("DATA DA VENDA: ", dados_venda["data"])
        print("VALOR DA VENDA: ", dados_venda["valor"])
        print("\n")

    def seleciona_venda(self):
        codigo = input("Código da venda que deseja selecionar: ")
        return codigo

    def mostra_mensagem(self, msg):
        print(msg)
