class TelaProduto():
    def tela_opcoes(self):
        print("-------- PRODUTO --------")
        print()
        print("1 - Incluir produto")
        print("2 - Alterar preço de venda do produto")
        print("3 - Alterar quantidade de estoque do produto")
        print("4 - Listar produto")
        print("5 - Excluir produto")
        print("0 - Retornar")

        opcao = int(input("Escolha a opção: "))
        print()
        return opcao

    def pega_dados_produto(self):
        print("-------- DADOS PRODUTO --------")
        nome = input("Nome: ")
        codigo = input("Codigo: ")
        preco_venda = input("Preco de Venda: ")
        quant_estoque = input("Quantidade comprada: ")
        print()
        
        return {"nome": nome, "codigo": codigo, "preco_venda": preco_venda, "quant_estoque": quant_estoque}  
    
    def pega_quantidade(self):
        print("----- ALTERAR QUANTIDADE NO ESTOQUE ------")
        quantidade_nova = input("Digite a quantidade atual: ")
        print()
        return quantidade_nova
    
    def pega_preco(self):
        print("-------- ALTERAR PREÇO DE VENDA DO PRODUTO --------")
        preco_novo = input("Digite o novo preço de venda do produto: ")
        print()
        return preco_novo

    def mostra_produto(self, dados_produto):
        print("NOME:", dados_produto["nome"])
        print("CÓDIGO:", dados_produto["codigo"])
        print("PREÇO:", dados_produto["preco_venda"])
        print("QUANTIDADE NO ESTOQUE:", dados_produto["quant_estoque"])
        print()

    def seleciona_produto(self): 
        codigo = input("Código do produto que deseja selecionar: ")
        print()
        return codigo

    def mostra_mensagem(self, msg):
        print(msg)
