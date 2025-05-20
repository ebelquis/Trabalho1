class TelaPessoa():
    def tela_opcoes(self):
        print("-------- PESSOAS ----------")
        print("Escolha a opção")
        print("1 - Incluir Cliente")
        print("2 - Incluir Vendedor")
        print("3 - Listar Clientes")
        print("4 - Excluir Cliente")
        print("5 - Listar Vendedores")
        print("6 - Excluir Vendedor")
        print("0 - Retornar")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def pega_dados_pessoa(self):
        print("-------- DADOS PESSOA ---------")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        celular = input("Celular: ")

        return {"nome": nome, "cpf": cpf, "celular": celular}

    def mostra_cliente(self, dados_cliente):
        print("------CLIENTE------")
        print("NOME DO CLIENTE: ", dados_cliente["nome"])
        print("CPF DO CLIENTE: ", dados_cliente["cpf"])
        print("TELEFONE DO CLEINTE: ", dados_cliente["telefone"])
        print("\n")

    def mostra_vendedor(self, dados_vendedor):
        print("------VENDEDOR------")
        print("NOME DO VENDEDOR: ", dados_vendedor["nome"])
        print("CPF DO VENDEDOR: ", dados_vendedor["cpf"])
        print("TELEFONE DO VENDEDOR: ", dados_vendedor["telefone"])
        print("VALOR VENDIDO TOTAL DO VENDEDOR: ", dados_vendedor["valor_vendido_total"])
        print("\n")
    
    def seleciona_pessoa(self):
        cpf = input("CPF da pessoa que deseja selecionar: ")
        return cpf

    def mostra_mensagem(self, msg):
        print(msg)