class TelaSistema:

    def teste_numero_opcoes(self, mensagem=" ", valores_validos = None):
        while True:
            valor_recebido = input(mensagem)
            try:
                valor_recebido_tipo = int(valor_recebido)
                if valores_validos and valor_recebido_tipo not in valores_validos:
                    raise ValueError
                return valor_recebido_tipo
            except ValueError:
                print("Você não digitou um valor aceitavel, digite novamente")

    def tela_opcoes(self):
        print()
        print("======== SISTEMA DE ESTOQUE DA A5 ========")
        print()
        print("1 - Realizar venda")
        print("2 - Fornecedor")
        print("3 - Produto")
        print("4 - Pessoa")
        print("5 - Realizar pedido")
        print("0 - Finalizar sistema")
<<<<<<< HEAD
        
        opcao = self.teste_numero_opcoes("Escolha a opcao: ", [0, 1, 2, 3, 4, 5])
        print("\n")
=======
        print()
        opcao = int(input("Escolha a opção: "))
        print()
>>>>>>> bb35d15247fd653159199aa5c0d51242b2e10cbe
        return opcao
