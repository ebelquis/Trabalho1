class TelaProduto():
    def tela_opcoes(self):
        print("-------- PRODUTO ----------")
        print("Escolha a opcao")
        print("1 - Incluir Produto")
        print("2 - Alterar Valor Do Produto")
        print("3 - Alterar Quantidade De Estoque Do Produto")
        print("4 - Listar Produto")
        print("5- Excluir Produto")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_produto(self):
        print("-------- DADOS PRODUTO ----------")
        nome = input("Nome: ")
        codigo = input("Codigo: ")
        preco_venda = input("Preco de Venda: ")
        quant_estoque = input("Quantidade comprada: ")
        
        return {"nome": nome, "codigo": codigo, "preco_venda": preco_venda, "quant_estoque": quant_estoque}  
    
    def pega_dados_produto_alterar(self):
        print("-------- VALOR PARA ALTERAR ----------")
        valor = input("Preco venda / Quantidade a mais no estoque : ")
        
        return {"valor": valor}

    def mostra_produto(self, dados_produto):
        print("NOME DO PRODUTO ", dados_produto["nome"])
        print("CODIGO DO PRODUTO: ", dados_produto["codigo"])
        print("PRECO DO PRODUTO: ", dados_produto["preco_venda"])
        print("QUANTIDADE NO ESTOQUE DO PRODUTO: ", dados_produto["quant_estoque"])
        print("\n")

    def seleciona_produto(self):
        codigo = input("Código do produto que deseja selecionar: ")
        return codigo

    def mostra_mensagem(self, msg):
        print(msg)