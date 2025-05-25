from excessoes.TesteNumeroOpcoesException import TesteNumeroOpcoes

class TelaProduto(TesteNumeroOpcoes):

    def __init__(self):
        pass

    def teste_do_float(self, mensagem=" "):
            while True:
                valor_recebido = input(mensagem)
                try:
                    valor_recebido_tipo = float(valor_recebido)
                    return valor_recebido_tipo
                except ValueError:
                    print("Por favor, escreva somente com numeros. (erro na digitação)")


    def teste_do_inteiro(self, mensagem=" "):
            while True:
                valor_recebido = input(mensagem)
                try:
                    valor_recebido_tipo = int(valor_recebido)
                    return valor_recebido_tipo
                except ValueError:
                    print("Por favor, escreva somente com numeros inteiros. Exemplo 1234 (erro na digitação)")

    def tela_opcoes(self):
        print("-------- PRODUTO --------")
        print()
        print("1 - Incluir produto")
        print("2 - Alterar preço de venda do produto")
        print("3 - Alterar quantidade de estoque do produto")
        print("4 - Listar produto(s)")
        print("5 - Excluir produto")
        print("0 - Retornar")

<<<<<<< HEAD
        opcao = self.teste_numero_opcoes("Escolha a opcao: ", [0, 1, 2, 3, 4, 5])
        print("\n")
=======
        opcao = int(input("Escolha a opção: "))
        print()
>>>>>>> bb35d15247fd653159199aa5c0d51242b2e10cbe
        return opcao

    def pega_dados_produto(self):
        print("-------- DADOS PRODUTO --------")
        print()
        nome = input("Nome: ")
<<<<<<< HEAD
        codigo_produto = self.teste_do_inteiro("codigo_produto: ")
        preco_venda = self.teste_do_float("Preco de Venda: ")
        quant_estoque = self.teste_do_inteiro("Quantidade comprada: ")
        print("\n")
=======
        codigo = input("Codigo: ")
        preco_venda = input("Preco de Venda (R$): ")
        quant_estoque = input("Quantidade comprada: ")
        print()
>>>>>>> bb35d15247fd653159199aa5c0d51242b2e10cbe
        
        return {"nome": nome, "codigo_produto": codigo_produto, "preco_venda": preco_venda, "quant_estoque": quant_estoque}  
    
<<<<<<< HEAD
    def pega_dados_produto_alterar(self):
        print("-------- VALOR PARA ALTERAR ----------")
        valor = self.teste_do_float("Preco venda / Quantidade a mais no estoque : ")
        print("\n")
        return valor

    def mostra_produto(self, dados_produto):
        print("NOME DO PRODUTO ", dados_produto["nome"])
        print("CODIGO DO PRODUTO: ", dados_produto["codigo_produto"])
        print("PRECO DO PRODUTO: ", dados_produto["preco_venda"])
        print("QUANTIDADE NO ESTOQUE DO PRODUTO: ", dados_produto["quant_estoque"])
        print("\n")

    def seleciona_produto(self):
        print("-------- SELECIONADOR DE PRODUTO ----------")
        codigo = self.teste_do_inteiro("Código do produto que deseja selecionar: ")
        print("\n")
=======
    def pega_quantidade(self):
        print("----- ALTERAR QUANTIDADE NO ESTOQUE ------")
        print()
        quantidade_nova = input("Digite a quantidade atual: ")
        print()
        return quantidade_nova
    
    def pega_preco(self):
        print("-------- ALTERAR PREÇO DE VENDA DO PRODUTO --------")
        print()
        preco_novo = input("Digite o novo preço de venda do produto: ")
        print()
        return preco_novo

    def mostra_produto(self, dados_produto):
        print("NOME:", dados_produto["nome"])
        print("CÓDIGO:", dados_produto["codigo"])
        print(f"PREÇO: R${dados_produto["preco_venda"]:.2f}")
        print("QUANTIDADE NO ESTOQUE:", dados_produto["quant_estoque"])
        print()

    def seleciona_produto(self): 
        codigo = input("Código do produto que deseja selecionar: ")
        print()
>>>>>>> bb35d15247fd653159199aa5c0d51242b2e10cbe
        return codigo

    def mostra_mensagem(self, msg):
        print(msg)
<<<<<<< HEAD
        print("\n")
=======
        print()
>>>>>>> bb35d15247fd653159199aa5c0d51242b2e10cbe
