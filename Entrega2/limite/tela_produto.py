from excessoes.OpcaoErroException import OpcaoErroException

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

        try:
            opcao = int(input("Escolha a opcao: "))
            if opcao not in [0, 1, 2, 3, 4, 5]:
                raise OpcaoErroException()
            return opcao
        except OpcaoErroException as e:
            self.mostra_mensagem(e)

    def pega_dados_produto(self):
        print("-------- DADOS PRODUTO ----------")

        while True:
            try:
                nome = str(input("Nome:"))
                break
            except ValueError:
                print("nome inválido. Insira um nome valido.")

        while True:
            try:
                codigo = int(input("Codigo:"))
                break
            except ValueError:
                print("codigo inválido. Insira um valor valido.")

        while True:
            try:
                preco_venda = int(input("preco_venda:"))
                break
            except ValueError:
                print("preco inválido. Insira um valor valido.")

        while True:
            try:
                quant_estoque = int(input("quant_estoque:"))
                break
            except ValueError:
                print("quantidade inválida. Insira um valor valido.")
        
        return {"nome": nome,
                "codigo": codigo,
                "preco_venda": preco_venda,
                "quant_estoque": quant_estoque}  
    
    def pega_dados_produto_alterar(self):
        print("-------- VALOR PARA ALTERAR ----------")
        while True:
            try:
                valor = int(input("Preco venda / Quantidade a mais no estoque : "))
                break
            except ValueError:
                print("Esse valor é invalido. Digite novamente")
        return {"valor": valor}

    def mostra_produto(self, dados_produto):
        print("NOME DO PRODUTO ", dados_produto["nome"])
        print("CODIGO DO PRODUTO: ", dados_produto["codigo"])
        print("PRECO DO PRODUTO: ", dados_produto["preco_venda"])
        print("QUANTIDADE NO ESTOQUE DO PRODUTO: ", dados_produto["quant_estoque"])
        print("\n")

    def seleciona_produto(self):
        while True:
            try:
                codigo = int(input("Código do produto que deseja selecionar: "))
            except ValueError:
                print("O codigo nao esta ecrito corretamente. Digite Novamente!")
            return codigo

    def mostra_mensagem(self, msg):
        print(msg)